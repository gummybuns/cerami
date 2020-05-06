from ..search_attribute import SearchAttribute

class Returnable(object):
    """A mixin to add the returns method"""

    def returns(self, value):
        """return the Request setup with ReturnValues attribute

        Adds the ReturnValues to the request attributes dict

        Arguments
        value -- NONE | ALL_OLD | UPDATED_OLD | ALL_NEW | UPDATED_NEW

        Returns:
        the instance of this class
        """
        self.add_attribute(
            SearchAttribute,
            'ReturnValues',
            value)
        return self
