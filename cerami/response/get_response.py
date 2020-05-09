from .response import Response

class GetResponse(Response):
    """A Response class to handle GetRequest"""
    def __init__(self, response, reconstructor):
        """constructor for GetResponse

        Arguments:
        response -- a dict from DynamoDB typically from a get_item request
        reconstructor -- a Reconstructor object to help interpret data
        """
        super(GetResponse, self).__init__(response, reconstructor)
        try:
            self.item = self.reconstructor.reconstruct(self._raw['Item'])
        except KeyError:
            self.item = None
