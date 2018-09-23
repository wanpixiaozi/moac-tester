from __future__ import unicode_literals

import pytest

from moac_tester import (
    MoacTester,
    MockBackend,
)

from moac_tester.utils.backend_testing import (
    BaseTestBackendDirect,
)


@pytest.fixture
def eth_tester():
    backend = MockBackend()
    return MoacTester(backend=backend)


class TestMockBackendDirect(BaseTestBackendDirect):
    supports_evm_execution = False

    @pytest.mark.skip(reason="receipt status not supported in MockBackend")
    def test_get_transaction_receipt_byzantium(self, eth_tester, test_transaction):
        pass

    @pytest.mark.skip(reason="receipt status not supported in MockBackend")
    def test_get_transaction_receipt_byzantium(self, eth_tester, test_transaction):
        pass
