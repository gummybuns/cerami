from .dynamo_search_interface import DynamoSearchInterface
from .search_attribute import DictAttribute
from ..dynamo_response import DynamoSaveResponse

class DynamoPutInterface(DynamoSearchInterface):
    def execute(self):
        response = self.client.put_item(**self.build())
        return DynamoSaveResponse(response, self.reconstructor)

    def item(self, item_dict):
        """add the item_dict to the search_attributes"""
        self.add_attribute(DictAttribute, 'Item', item_dict)
        return self


