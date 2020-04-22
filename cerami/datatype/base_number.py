from .base_datatype import DynamoDataType
from .mapper import NumberMapper
from .expression import ArithmeticExpression

class BaseNumber(DynamoDataType):
    @property
    def condition_type(self):
        return "N"

    def add(self, value):
        return ArithmeticExpression('+', self, value)

    def subtract(self, value):
        return ArithmeticExpression('-', self, value)

    @property
    def mapper(self):
        return NumberMapper(self)
