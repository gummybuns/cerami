from .response import Response

class SearchResponse(Response):
    """A Response class to handle SearchRequest

    A SearchResponse is returned from a ScanRequest or QueryRequest
    """
    def __init__(self, response, reconstructor):
        """Constructor for SearchResponse

        Arguments:
        response -- a dict from DynamoDB typically from a scan or query request
        reconstructor -- a Reconstructor object to help interpret data
        """
        super(SearchResponse, self).__init__(response, reconstructor)
        self.count = self._raw['Count']
        self.scanned_count = self._raw['ScannedCount']
        self.last_evaluated_key = self._raw.get('LastEvaluatedKey')
        self._items = self._raw.get('Items', [])

    @property
    def items(self):
        """A generator to get individual items from the response

        Whenever an item is yielded, it will reconstruct the item using the reconstructor

        Returns:
        A generator to iterate over items in the response
        """
        for item in self._items:
            yield self.reconstructor.reconstruct(item)
