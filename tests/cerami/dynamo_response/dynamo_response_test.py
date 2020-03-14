from mock import Mock
from tests.helpers.testbase import TestBase
from cerami.dynamo_response import DynamoResponse

class TestDynamoResponse(TestBase):
    def test__init__(self):
        mocked_reconstructor = Mock()
        db_response = {'test': True}
        resp = DynamoResponse(db_response, mocked_reconstructor)
        assert resp._raw == db_response
        assert resp.reconstructor == mocked_reconstructor
