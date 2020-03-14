from mock import patch, call, Mock
from tests.helpers.testbase import TestBase
import cerami.datatype as dt
from cerami.model import Model
from cerami.datatype import String
from cerami.datatype.expression import EqualityExpression
from cerami.dynamo_search_interface.search_attribute import (
    SearchAttribute,
    DictAttribute,
    QueryExpressionAttribute,)
from cerami.dynamo_search_interface import (
    DynamoSearchInterface)

class TestModel(Model):
    test = String()

class TestDynamoSearchInterface(TestBase):
    def setUp(self):
        self.client = Mock()
        self.search_interface = DynamoSearchInterface(self.client,
                                                      tablename='testtable')

    def test_add_attribute(self):
        """it calls add for the search attribute"""
        with patch("cerami.dynamo_search_interface.search_attribute.SearchAttribute.add") as add:
            self.search_interface.add_attribute(SearchAttribute,
                                                'Test',
                                                123)
            assert isinstance(
                self.search_interface.search_attributes['Test'],
                SearchAttribute)
            add.assert_called_with(123)

    def test_filter(self):
        """it adds FilterExpression, ExpresionAttributeNames,
        ExpressionAttributeValues"""
        with patch("cerami.dynamo_search_interface.DynamoSearchInterface.add_attribute") as add:
            expression = TestModel.test.eq('123')
            names = {}
            names[expression.expression_attribute_name] = 'test'

            self.search_interface.filter(expression)
            calls = [
                call(QueryExpressionAttribute,
                     'FilterExpression',
                     expression),
                call(DictAttribute,
                     'ExpressionAttributeNames',
                     names),
                call(DictAttribute,
                     'ExpressionAttributeValues',
                     expression.value_dict())
            ]
            add.assert_has_calls(calls)

    def test_build(self):
        """returns a dict for all search_attributes"""
        self.search_interface.add_attribute(SearchAttribute,
                                            'Test',
                                            123)
        built = self.search_interface.build()
        expected = {
            "TableName": "testtable",
            "Test": 123,
        }
        assert built == expected

    def test_return_values(self):
        """it calls add_attribute with the value"""
        self.search_interface.add_attribute = Mock()
        self.search_interface.return_values('test')
        self.search_interface.add_attribute.assert_called_with(
            SearchAttribute,
            'ReturnValues',
            'test')
