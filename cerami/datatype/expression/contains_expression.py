from .base_expression import BaseExpression

class ContainsExpression(BaseExpression):
    """A class to generate a `CONTAINS` expression for querying/scanning

    `ContainsExpression` *cannot* be used in queries. It can only be used in filter
    expressions and condition expressions.

    For example::

        # You can use Person.email.contains instead!
        expression = ContainsExpression(Person.email, "test")
        Email.scan.filter(expression).build()
        {
            "TableName": "people",
            "FilterExpression": "contains(#__email, :_email_xfdww)",
            "ExpressionAttributeNames": {
                "#__email": "email"
            },
            "ExpressionAttributeValues": {
                ":_email_xfdww": {
                    "S": "test@test.com"
                }
            }
        }
    """
    def __init__(self, datatype, value, is_set=False):
        """constructor for BeginsWithExpression

        Parameters:
            datatype: a DynamoDataType that the expression is for
            value: check value to check if the datatype of an item contains
            is_set: a flag to know if the ContainsExpression is for a Set
        """
        super(ContainsExpression, self).__init__('contains', datatype, value)
        self.is_set = is_set

    def __str__(self):
        attr_name = self.expression_attribute_name
        if hasattr(self.datatype, '_index'):
            attr_name = "{}[{}]".format(attr_name, self.datatype._index)
        return "{expression}({attr_name}, {value})".format(
            attr_name=attr_name,
            expression=self.expression,
            value=self.expression_attribute_value_name)

    def value_dict(self):
        """return the expected dict for expression-attribute-values

        This overrides the BaseExpression because the SetMapper cannot use the default
        method for creating this expression. When a SetMapper is the datatype, it must
        instead use the inner datatype to map the value directly.
        """
        if self.is_set:
            res = {}
            res[self.expression_attribute_value_name] = self.datatype.datatype.translator.to_dynamodb(self.value)
            return res
        else:
            return super(ContainsExpression, self).value_dict()
