from .dynamo_response import DynamoResponse

class DynamoGetResponse(DynamoResponse):
    def __init__(self, response, reconstructor):
        super(DynamoGetResponse, self).__init__(response, reconstructor)
        try:
            self.item = self.reconstructor.reconstruct(self._raw['Item'])
        except KeyError:
            self.item = None
