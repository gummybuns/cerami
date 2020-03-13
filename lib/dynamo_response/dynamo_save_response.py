from .dynamo_response import DynamoResponse

class DynamoSaveResponse(DynamoResponse):
    def __init__(self, response, reconstructor):
        super(DynamoSaveResponse, self).__init__(response, reconstructor)
        try:
            self.item = self.reconstructor.reconstruct(self._raw['Attributes'])
        except KeyError:
            self.item = None
