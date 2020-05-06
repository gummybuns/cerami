from ..search_attribute import DictAttribute

class Keyable(object):
    """A mixin to add the key method"""

    def key(self, *expressions):
        """return a new Request setup with the Key attribute

        Adds the Ley to the request_attributes dict

        Arguments:
        expressions -- a list of BaseExpressions

        Returns:
        the instance of this class
        """
        for expression in expressions:
            key_dict = {}
            key_dict[expression.datatype.column_name] = expression.attribute_map()
            self.add_attribute(DictAttribute, 'Key', key_dict)
        return self
