import random
import string

class BaseExpression(object):
    """The base class for all expressions.

    Expressions are objects that are generated by datatypes that are used in requests -
    querying, filtering, updating etc.

    Attributes:
        expression: a string representing to define the type of expression. For example,
            it can be `"="` to perform an equality expression
        datatype: a DynamoDataType that the expresion is for
        value: anything that is used in the expression
        expression_attribute_name: DynamoDB has a list of reserved words, but since the
            list is so long and impossible to remember, there are likely collisions with
            a table's columns. For this reason, most DynamoDB requests has an option
            `ExpressionAttributeNames`, which is a dict which makes an arbitrary string
            back to the column name. The `ExpressionAttributeName` must start with a
            `"#"`.

            For example, you may have a column called `"action"` (which is a reserved
            word). An `expression_attribute_name` is automatically generated that prevents
            an error.
        expression_attribute_value_name: DynamoDB requires all of its Expressions to use
            a unique string that gets mapped to its ExpressionAttributeValues dict. This
            string must start with a `":"`. All `expression_attribute_value_names` include
            the column_name of the datatype and a series of random characters to ensure
            there are no collisions when multiple expressions are used in a request

    For example::
   
        expression = BaseExpression("=", Parent.email, "test@test.com")
        expression.expression_attribute_name # <== "#__email"
        expression.expression_attribute_value_name # <== ":_email_xfdww"

        Parent.query.filter(expression).build()
        {
            "TableName": "people",
            "FilterExpression": "#__email = :_email_xfdww",
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
    def __init__(self, expression, datatype, value):
        """constructor for the BaseExpression

        Parameters:
            expression: a string representing to define the type of expression. For
                example, it can be `"="` to perform an equality expression
            datatype: a DynamoDataType that the expresion is for
            value: anything that is used in the expression
        """
        self.expression = expression
        self.datatype = datatype
        self.value = value
        column_name_safe = datatype.column_name.replace('.', '_')
        self.expression_attribute_name = "#__{}".format(column_name_safe)
        self.expression_attribute_value_name = self._generate_variable_name(
            column_name_safe)

    def __str__(self):
        """convert the expression into a string

        it will automatically update the expression attribute name to include the
        index when it is included in the datatype for lists.

        Returns:
            a string of the expression that can be used in Requests
        """
        attr_name = self.expression_attribute_name
        if hasattr(self.datatype, '_index'):
            attr_name = "{}[{}]".format(attr_name, self.datatype._index)
        return "{attr_name} {expression} {value_name}".format(
            attr_name=attr_name,
            expression=self.expression,
            value_name=self.expression_attribute_value_name)

    def attribute_map(self):
        """return the value and its condition_type by calling a Datatype Translator

        This is only used by Keyable right now. But i think this should be deprecated
        because its confusing and doesnt really add any value
        """
        return self.datatype.translator.to_dynamodb(self.value)

    def value_dict(self):
        """return the expected dict for expression-attribute-values

        This is used by many of different requests when building search_attributes. Most
        requests require the `ExpressionAttributeValue` option. This will build that
        corresponding property for this particular expression

        Returns:
            a dict that can be used in ExpressionAttributeValue options

        For example::

            expression = Expression("=", Parent.name, "Mom")
            expression.value_dict() # <== {":_name_abc12":{"S": "Mom"}}
        """
        res = {}
        res[self.expression_attribute_value_name] = self.datatype.translator.to_dynamodb(self.value)
        return res

    def _generate_variable_name(self, column_name):
        """return a random name for the value"""
        letters = string.ascii_lowercase
        random_letters = ''.join(random.choice(letters) for i in range(5))
        return ":_{}_{}".format(column_name, random_letters)
