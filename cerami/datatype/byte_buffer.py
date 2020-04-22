from .base_datatype import DynamoDataType
from .mapper import ByteMapper

class ByteBuffer(DynamoDataType):
    @property
    def condition_type(self):
        return "B"

    @property
    def mapper(self):
        return ByteMapper(self)

    def build(self, val):
        val = val or self._get_default()
        if isinstance(val, bytes) or val is None:
            return val
        return val.encode('utf-8')

    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)
