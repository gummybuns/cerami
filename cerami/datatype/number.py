from .base_number import BaseNumber

class Number(BaseNumber):
    def as_item(self, val):
        return val

    def as_dict(self, val):
        return self.as_item(val)

