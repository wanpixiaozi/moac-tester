import os
import sys
import warnings

from moac_tester.utils.module_loading import (
    get_import_path,
    import_string,
)
from .mock import (   # noqa: F401
    MockBackend,
)


def get_chain_backend_class(backend_import_path=None):
    warnings.simplefilter('default')

    if backend_import_path is None:
        if 'MOAC_TESTER_CHAIN_BACKEND' in os.environ:
            backend_import_path = os.environ['MOAC_TESTER_CHAIN_BACKEND']
        else:
            warnings.warn(UserWarning(
                "Moac Tester: No backend was explicitely set, and no *full* "
                "backends were available.  Falling back to the `MockBackend` "
                "which does not support all EVM functionality.  Please refer to "
                "the `moac-tester` documentation for information on what "
                "backends are available and how to set them."
            ))
            backend_import_path = get_import_path(MockBackend)
    return import_string(backend_import_path)


def get_chain_backend(backend_class=None):
    if backend_class is None:
        backend_class = get_chain_backend_class()
    return backend_class()
