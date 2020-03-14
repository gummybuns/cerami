from mock import Mock, patch
from tests.helpers.testbase import TestBase
from cerami.dynamo_response import DynamoSearchResponse
from cerami.dynamo_search_interface import (
    DynamoQuerySearchInterface)

class TestDynamoQuerySearchInterface(TestBase):
    def setUp(self):
        self.mocked_client = Mock()
        self.search_interface = DynamoQuerySearchInterface(
            tablename="test",
            client=self.mocked_client)

    def test_execute(self):
        """it calls query with the build
        it returns a DynamoSearchResult"""
        with patch("cerami.dynamo_search_interface.DynamoQuerySearchInterface.build") as build:
            expected = {"fake": True}
            self.mocked_client.query.return_value = {
                'Count': 0,
                'ScannedCount': 0}
            build.return_value = expected
            res = self.search_interface.execute()
            self.mocked_client.query.assert_called_with(fake=True)
            assert isinstance(res, DynamoSearchResponse)

