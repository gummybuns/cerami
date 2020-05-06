from ..search_attribute import SearchAttribute

class Limitable(object):
    """A mixin to add the limit method"""

    def limit(self, limit_number):
        """return a new Request setup with the limit attribute

        Adds the Limit to the request_attributes dict

        Arguments:
        limit_number -- a number representing the maximum items to be returned

        Returns:
        the instace of this clase
        """
        self.add_attribute(
            SearchAttribute,
            'Limit',
            limit_number)
        return self
