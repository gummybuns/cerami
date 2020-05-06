from ..response import SearchResponse
from .mixins import BaseRequest, Filterable, Projectable, Limitable

class ScanRequest(BaseRequest, Filterable, Projectable, Limitable):
    """A class to perform the scan request"""

    def execute(self):
        """perform the scan request

        Returns:
        a SearchResponse built from the scan response
        """
        response = self.client.scan(**self.build())
        return SearchResponse(response, self.reconstructor)
