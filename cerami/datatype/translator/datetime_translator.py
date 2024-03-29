import dateutil.parser
from .base_datatype_translator import BaseDatatypeTranslator
from datetime import datetime, timezone

class DatetimeTranslator(BaseDatatypeTranslator):
    """A Translator class for Datetimes

    This translator is typically used with the ``Datetime`` datatype. This class will
    automatically convert the passed in datetime to UTC as is required by DynamoDB

    https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBMapper.DataTypes.html

    For example::

        import datetime
        translator  = DatetimeTranslator(String())
        translator.to_dynamodb(datetime.datetime.now())
        {'S': '2020-05-22T00:03:46.664845+00:00'}

        translator.to_cerami({'S': '2020-05-22T00:03:46.664845+00:00'})
        datetime.datetime(2020, 5, 22, 0, 4, 33, 144061, tzinfo=tzutc())
    """

    def format_for_dynamodb(self, value):
        """Convert the datetime into an ISO 8601 string

        Parameters:
            value: a datetime object. Can be timezone aware or unaware

        Returns:
            a ISO 8601 string representation of the value in UTC
        """
        return value.replace(tzinfo=timezone.utc).isoformat()

    def format_for_cerami(self, value):
        """Convert the datetime string into a datetime object

        Since it uses ``dateutil.parser``, this should handle both
        ISO 8601 strings and timezone agnostic values, however
        if the record was created using the `format_for_dynamodb()` method, a
        utc timezone should automatically be included

        Parameters:
            value: A string representation of a datetime. Typically the value should be
                an ISO 8601 string

        Returns:
            a datetime object
        """
        return dateutil.parser.parse(value)
