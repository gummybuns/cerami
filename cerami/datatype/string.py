from .base_string import BaseString

class String(BaseString):
    def build(self, val):
        val = val or self._get_default()
        return val

    def as_item(self, val):
        return str(val)

    def as_dict(self, val):
        return self.as_item(val)


