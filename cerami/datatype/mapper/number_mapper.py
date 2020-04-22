from .string_mapper import StringMapper
from .base_datatype_mapper import BaseDatatypeMapper

class NumberMapper(BaseDatatypeMapper):
    def parse(self, mapped_dict):
        if mapped_dict.get('NULL') == True:
            return None
        return int(mapped_dict[self.datatype.condition_type])

    def resolve(self, value):
        return str(value)
