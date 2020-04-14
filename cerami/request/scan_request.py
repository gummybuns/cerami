from ..response import SearchResponse
from .mixins import BaseRequest, Filterable

class ScanRequest(BaseRequest, Filterable):
    def execute(self):
        response = self.client.scan(**self.build())
        return SearchResponse(response, self.reconstructor)
