from .dynamo_search_interface import DynamoSearchInterface
from .search_attribute import DictAttribute
from ..dynamo_response import DynamoDeleteResponse

class DynamoDeleteInterface(DynamoSearchInterface):
    def execute(self):
        response = self.client.delete_item(**self.build())
        return DynamoDeleteResponse(response, self.reconstructor)

    def key(self, *expressions):
        for expression in expressions:
            key_dict = {}
            key_dict[expression.datatype.column_name] = expression.attribute_map()
            self.add_attribute(DictAttribute, 'Key', key_dict)
        return self