from .mixins import BaseRequest
from .search_attribute import DictAttribute
from ..response import SaveResponse

class PutRequest(BaseRequest):
    """A class to perform the put_item request"""

    def execute(self):
        """perform the put_item request

        Returns:
        a SaveResponse object built from the put_item response
        """
        response = self.client.put_item(**self.build())
        return SaveResponse(response, self.reconstructor)

    def item(self, item_dict):
        """add the item_dict to the search_attributes

        Adds the Item to the request_attributes dict

        Arguments:
        item_dict -- a dict with a format matching the format DynamoDb
            expects data. Typically this is done though Model.as_item()

        Returns:
        the instance of this class
        """
        self.add_attribute(DictAttribute, 'Item', item_dict)
        return self
