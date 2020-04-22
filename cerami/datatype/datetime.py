import dateutil.parser
from datetime import datetime
from .base_string import BaseString

class Datetime(BaseString):
    def build(self, val):
        val = val or self._get_default()
        if isinstance(val, datetime) or val is None:
            return val
        return dateutil.parser.parse(val)

    def as_item(self, val):
        return val.isoformat()

    def as_dict(self, val):
        return self.as_item(val)

