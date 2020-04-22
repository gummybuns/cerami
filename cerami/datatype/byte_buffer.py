from .base_datatype import DynamoDataType
from .mapper import ByteMapper

class ByteBuffer(DynamoDataType):
    def __init__(self, mapper_cls=ByteMapper, **kwargs):
        super(ByteBuffer, self).__init__(mapper_cls=mapper_cls, condition_type="B", **kwargs)

    def build(self, val):
        val = val or self._get_default()
        if isinstance(val, bytes) or val is None:
            return val
        return val.encode('utf-8')

    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)
