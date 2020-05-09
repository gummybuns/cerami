from .search_attribute import SearchAttribute

class DictAttribute(SearchAttribute):
    """A class for representing SearchAttributes as a dict"""

    def __init__(self, name, value=None):
        """constructor for the SearchAttribute

        Arguments:
        name - a string representing the option for the Request.

        Keyword Arguments
        value - it should be a dict, or will default to an empty one
        """
        value = value or {}
        super(DictAttribute, self).__init__(name, value)

    def add(self, value_dict):
        """Update the self.value with the value_dict
        
        This allows for chaining or the same call to overwrite any keys
        that were previously present with the new values represented in
        value_dict
        """
        self.value.update(value_dict)
