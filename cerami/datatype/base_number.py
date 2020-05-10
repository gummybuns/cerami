from .base_datatype import DynamoDataType
from .mapper import NumberMapper
from .expression import ArithmeticExpression

class BaseNumber(DynamoDataType):
    """A Base class for all Number datatypes"""

    def __init__(self, mapper_cls=NumberMapper, default=None, column_name=""):
        """constructor for the BaseNumber

        Arguments:
        default -- a default value for the column. It can be a value or function
        column_name -- a string defining the name of the column on the table
        mapper_cls -- A mapper class to manipulate data to/from dynamodb.
            Defaults to the NumberMapper
        """
        super(BaseNumber, self).__init__(
            mapper_cls=mapper_cls,
            condition_type="N",
            default=default,
            column_name=column_name)

    def add(self, value):
        return ArithmeticExpression('+', self, value)

    def subtract(self, value):
        return ArithmeticExpression('-', self, value)
