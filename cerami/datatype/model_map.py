from copy import copy
from .base_datatype import DynamoDataType
from .mapper import ModelMapper

class ModelMap(DynamoDataType):
    def __init__(self, model_cls, default=None, **kwargs):
        super(ModelMap, self).__init__(**kwargs)
        self.model_cls = model_cls
        for column in self.model_cls._columns:
            setattr(self, column.column_name, copy(column))

    @property
    def condition_type(self):
        return "M"

    @property
    def mapper(self):
        return ModelMapper(self)

    def build(self, val):
        val = val or self._get_default()
        if val == None:
            return None
        if isinstance(val, dict):
            return self.model_cls(data=val)
        elif isinstance(val, self.model_cls):
            return val
        else:
            raise ValueError("build must receive a dict or Model")

    def as_dict(self, val):
        return val.as_dict()

    def as_item(self, val):
        return val.as_item()

    def set_column_name(self, val):
        super(ModelMap, self).set_column_name(val)
        for name, attr in self.__dict__.items():
            if isinstance(attr, DynamoDataType):
                new_name = val + "." + name
                attr.set_column_name(new_name)


