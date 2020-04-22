from .dynamic import List
from .mapper import UniformListMapper

class UniformList(List):
    def __init__(self, datatype, **kwargs):
        super(UniformList, self).__init__(**kwargs)
        self.datatype = datatype

    @property
    def mapper(self):
        return UniformListMapper(self.datatype.mapper)

    def build(self, val=None):
        if val == None:
            return val
        if not isinstance(val, list):
            raise ValueError("{} is not a list".format(val))
        return [self.datatype.build(i) for i in val]

    def index(self, idx):
        """return an expression attribute of the inner datatype
        sets the index value on the expression attribute 
        """
        datatype_cls = type(self.datatype)
        dt = datatype_cls(column_name=self.column_name)
        dt._index = idx
        return dt

    def as_item(self, val):
        return [self.datatype.as_item(i) for i in val]

    def as_dict(self, val):
        return [self.datatype.as_dict(i) for i in val]

