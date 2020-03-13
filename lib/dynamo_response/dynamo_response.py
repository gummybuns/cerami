class DynamoResponse(object):
    def __init__(self, response, reconstructor):
        self._raw = response
        self.reconstructor = reconstructor
