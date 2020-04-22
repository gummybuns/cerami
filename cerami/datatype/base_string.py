from .base_datatype import DynamoDataType
from .mapper import StringMapper

class BaseString(DynamoDataType):
    """The base String Datatype"""
    @property
    def condition_type(self):
        return "S"

    @property
    def mapper(self):
        return StringMapper(self)
