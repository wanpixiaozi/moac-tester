import pkg_resources
import sys

from .main import (  # noqa: F401
    MoacTester
)

from .backends import (  # noqa: F401
    MockBackend
)


if sys.version_info.major < 3:
    raise EnvironmentError("moac-tester only supports Python 3")


__version__ = pkg_resources.get_distribution("moac-tester").version
