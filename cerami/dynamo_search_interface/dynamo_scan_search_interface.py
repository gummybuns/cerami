from .dynamo_search_interface import DynamoSearchInterface
from ..dynamo_response import DynamoSearchResponse

class DynamoScanSearchInterface(DynamoSearchInterface):
    def execute(self):
        response = self.client.scan(**self.build())
        return DynamoSearchResponse(response, self.reconstructor)
