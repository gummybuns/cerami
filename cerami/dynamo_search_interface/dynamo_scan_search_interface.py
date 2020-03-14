from .dynamo_search_interface import DynamoSearchInterface
from ..response import SearchResponse

class DynamoScanSearchInterface(DynamoSearchInterface):
    def execute(self):
        response = self.client.scan(**self.build())
        return SearchResponse(response, self.reconstructor)
