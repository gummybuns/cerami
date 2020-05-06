from copy import copy
from ...reconstructor import RawReconstructor
from ..search_attribute import SearchAttribute

class BaseRequest(object):
    """The Base Class for all requests

    It provides the default constructor and methods for building
    requests.
    """

    def __init__(self, client, tablename="", request_attributes=None, reconstructor=None):
        """constructor for base request

        Arguments:
        client -- An boto3.client('dynamodb')

        Keyword Arguments:
        tablename -- the name of the table to perform the request on
        request_attributes -- a dict of SearchAttribute objects whose
            keys represent options that can be passed to client upon execution
            For example, it may include a FilterExpression key whose value is
            a SearchAttribute that resolves to a string of filters
        reconstructor -- a Reconstructor object
        """
        self.request_attributes = copy(request_attributes or {})
        self.client = client
        self.reconstructor = reconstructor or RawReconstructor()
        if tablename:
            self.add_attribute(SearchAttribute, 'TableName', tablename)

    def __str__(self):
        return self.build().__str__()

    def add_attribute(self, attr_class, name, value):
        """add a search attribute to a to the request_attributes dict

        Arguments:
        attr_class -- a SearchAttribute class
        name -- the name of the attribute
        value -- the value that will be added to the SearchAttribute
        """
        request_attribute = self.request_attributes.get(name, attr_class(name))
        request_attribute.add(value)
        self.request_attributes[name] = request_attribute

    def build(self):
        """build the dict used by dynamodb

        Returns:
        a dict whose keys matching the keys of the request_attributes
            and whose values are string versions of each attribute
        """
        return dict((k, v.build()) for k, v in self.request_attributes.items())

