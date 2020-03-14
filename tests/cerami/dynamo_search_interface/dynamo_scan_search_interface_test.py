from mock import Mock, patch
from tests.helpers.testbase import TestBase
from cerami.response import SearchResponse
from cerami.dynamo_search_interface import (
    DynamoScanSearchInterface)

class TestDynamoScanSearchInterface(TestBase):
    def setUp(self):
        self.mocked_client = Mock()
        self.search_interface = DynamoScanSearchInterface(
            tablename="test",
            client=self.mocked_client)

    def test_execute(self):
        """it calls scan with the build
        it returns a DynamoSearchResult"""
        with patch("cerami.dynamo_search_interface.DynamoScanSearchInterface.build") as build:
            expected = {"fake": True}
            self.mocked_client.scan.return_value = {
                'Count': 0,
                'ScannedCount': 0}
            build.return_value = expected
            res = self.search_interface.execute()
            self.mocked_client.scan.assert_called_with(fake=True)
            assert isinstance(res, SearchResponse)
