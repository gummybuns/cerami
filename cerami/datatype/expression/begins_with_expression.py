from .base_expression import BaseExpression

class BeginsWithExpression(BaseExpression):
    """
    Generate a BEGINS WITH expression

    Email.query.key(Email.generated_email.begins_with("test"))
    ---
    dynamodb query \
        --table-name "Emails" \
        --key-condition-expression "begins_with(generated_email, :email1)"
        --expression-attribute-values '{":email1": {"S": "test"}}'
    """
    def __init__(self, datatype, value):
        super(BeginsWithExpression, self).__init__('begins_with', datatype, value)

    def __str__(self):
        attr_name = self.expression_attribute_name
        if hasattr(self.datatype, '_index'):
            attr_name = "{}[{}]".format(attr_name, self.datatype._index)
        return "{expression}({attr_name}, {value})".format(
            attr_name=attr_name,
            expression=self.expression,
            value=self.value)
