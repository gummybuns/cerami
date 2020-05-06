from ..search_attribute import (
    DictAttribute,
    QueryExpressionAttribute)

class Filterable(object):
    """A mixin to add the filter method"""

    def filter(self, *expressions):
        """return a new Request setup with filter attributes

        Adds the FilterExpression, ExpressionAttributeNames, and
        ExpressionAttributeValue to the request_attributes dict

        Arguments:
        expressions -- a list of BaseExpressions

        Returns:
        the instance of this class
        """
        for expression in expressions:
            names = {}
            names[expression.expression_attribute_name] = expression.datatype.column_name
            self.add_attribute(
                QueryExpressionAttribute,
                'FilterExpression',
                expression)
            self.add_attribute(
                DictAttribute,
                'ExpressionAttributeNames',
                names)
            self.add_attribute(
                DictAttribute,
                'ExpressionAttributeValues',
                expression.value_dict())
        return self
