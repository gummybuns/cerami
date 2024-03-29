from tests.helpers.testbase import TestBase
from cerami.model import Model
from cerami.datatype import (
    String,
    Number,
    ModelMap)
from cerami.datatype.translator import (
    ModelTranslator)

class TestModelMapper(TestBase):

    class FakeModel(Model):
        __tablename__ = 'test'
        test1 = String()
        test2 = Number()

    def setUp(self):
        super(TestModelMapper, self).setUp()
        self.dt = ModelMap(self.FakeModel)
        self.translator = ModelTranslator(self.dt)

    def test_format_for_dynamodb(self):
        """it should return the a dict with each column its resolved value"""
        model = self.FakeModel(test1='test', test2=2)
        expected = {'test1': {'S': 'test'}, 'test2': {'N': '2'}}
        res = self.translator.format_for_dynamodb(model)
        assert res == expected

    def test_to_dynamodb(self):
        """it should return the model as asn item"""
        model = self.FakeModel(test1="test", test2=2)
        res = self.translator.to_dynamodb(model)
        expected = {'M': {'test1': {'S': 'test'}, 'test2': {'N': '2'}}}
        assert res == expected

    def test_to_cerami(self):
        """it returns a model based on the passed dict"""
        value = {'M': {'test1': {'S': 'hello'}}}
        res = self.translator.to_cerami(value)
        assert isinstance(res, self.FakeModel)
        assert res.test1 == 'hello'
        assert res.test2 == None
        assert res.as_item() == {'test1': {'S': 'hello'}, 'test2': {'NULL': True}}
