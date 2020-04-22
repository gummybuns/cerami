from .base_number import BaseNumber

class Number(BaseNumber):
    def build(self, val):
        val = val or self._get_default()
        return val

    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)

