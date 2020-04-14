from .mixins import BaseRequest, Keyable
from ..response import GetResponse

class GetRequest(BaseRequest, Keyable):
    def execute(self):
        response = self.client.get_item(**self.build())
        return GetResponse(response, self.reconstructor)

