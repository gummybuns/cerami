from .base_string import BaseString

class String(BaseString):
    def as_item(self, val):
        return str(val)

    def as_dict(self, val):
        return self.as_item(val)


