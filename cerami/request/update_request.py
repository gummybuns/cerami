from .mixins import BaseRequest, Keyable, Returnable
from ..response import SaveResponse
from ..datatype.expression import (
    UpdateRemoveExpression,
    EqualityExpression)
from .search_attribute import (
    DictAttribute,
    UpdateAction,
    UpdateExpressionAttribute)


class UpdateRequest(BaseRequest, Keyable, Returnable):
    """A class to perform the update request"""

    def execute(self):
        """perform the update_item request

        Returns:
        a SaveResponse object built from the update_item response
        """
        response = self.client.update_item(**self.build())
        return SaveResponse(response, self.reconstructor)

    def set(self, *expressions):
        """Add a SET statement to the UpdateExpression

        The UpdateExpression is a comma separated list of instructions to perform on the
        table. SET will change the value or put the value if it does not exist.

        Arguments:
        expressions -- a list of BaseExpressions. In practice though, the expressions
            should all be EqualityExpressions using '=' (Model.column.eq('...'))

        Returns:
        the instance of this class
        """
        for expression in expressions:
            self.update_expression('SET', expression)
        return self

    def remove(self, *datatypes):
        """Add a REMOVE statement to the UpdateExpression

        The UpdateExpression is a comma separated list of instructions to perform on the
        table. REMOVE will delete the specified datatypes from the record. REMOVE can also
        be used to remove elements from a List datatype when used with List.index()

        Arguments:
        datatypes -- a list of DynamoDataType objects. (Model.column1, Model.column2, ...)

        Returns:
        ths instance of this class
        """
        for datatype in datatypes:
            expression = UpdateRemoveExpression(datatype)
            self.update_expression('REMOVE', expression)
        return self

    def add(self, datatype, value):
        """Add an ADD statement to the UpdateExpression

        AMAZON RECOMMENDS ONLY USING WITH NUMBERS AND SETS
        The UpdateExpression is a comma separated list of instructions to perform on the
        table. ADD can be used to change the value of the Number or add to a Set.

        Arguments:
        datatype -- a DynamoDataType object to change
        value -- the value to change the datatype
            For Numbers the value should be a number, it can be negative to subtract
            For Sets, the value should be an array

        Returns:
        the instance of this class
        """
        expression = EqualityExpression('', datatype, value)
        return self.update_expression('ADD', expression)

    def delete(self, datatype, value):
        """Add a DELETE statement to the UpdateExpression


        The UpdateExpression is a comma separated list of instructions to perform on the
        table. DELETE can be used to remove one or more elements from a Set only.

        Arguments:
        datatype -- a Set DynamoDatatype object
        value -- an array of values to remove from the set.

        Returns:
        the instance of the class
        """
        expression = EqualityExpression('', datatype, value)
        return self.update_expression('DELETE', expression)

    def update_expression(self, action, expression):
        """return a Request setup with the update expression attributes

        Adds the UpdateExpression, ExpressionAttributeNames and ExpressionAttributeValues
        to the request_attributes dict

        Arguments:
        action -- ADD | SET | DELETE | UPDATE
        expression -- a BaseExpression object

        Returns:
        the instance of the class
        """
        name = {}
        name[expression.expression_attribute_name] = expression.datatype.column_name
        self.add_attribute(UpdateExpressionAttribute,
                           'UpdateExpression',
                           UpdateAction(action, expression))
        self.add_attribute(DictAttribute,
                           'ExpressionAttributeNames',
                           name)
        self.add_attribute(DictAttribute,
                           'ExpressionAttributeValues',
                           expression.value_dict())
        return self
