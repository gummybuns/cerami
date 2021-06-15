Customizing Datatypes
=====================

While DynamoDB is limited in the datatypes it accepts, Cerami was built to easily create unique columns that can be translated back into one of the types required by DynamoDB.

All :doc:`DynamoDataType <../api/datatypes/base_datatype>` objects include a :doc:`Translator <../api/translators/index>` object whose purpose is to transform a models column to and from the format supported by DynamoDB. For example, DynamoDB supports numbers as columns, but these values must be converted to strings before submitted to the database. Looking at the `IntegerTranslator`:

.. code-block:: python

    class IntegerTranslator(BaseDatatypeTranslator):
        def format_for_dynamodb(self, value):
            """convert the number into a string"""
            return str(value)

        def format_for_cerami(self, value):
            """convert the number into an int"""
            return int(value)

The `format_for_dynamodb` method converts the column's number into a string before sending it to DynamoDB. The `format_for_cerami` method converts the database value back into a number when receiving it from DynamoDB.

Since every Translator defines methods to consistently convert data to and from DynamoDB, it can be leveraged to create custom data types.

Creating A UUID Datatype
------------------------
We want to store uuids in one of our tables. In order to do so, a new translator must be created. Like in the example above, all we need to do is override the format methods.

.. code-block:: python

    from uuid import UUID
    from cerami.datatype.translator import BaseDatatypeTranslator

    class UUID4Translator(BaseDatatypeTranslator):
        def format_for_dynamodb(self, value):
            """convert the uuid into a string"""
            return str(value)

        def format_for_cerami(self, value):
            """convert the string back into a uuid"""
            return UUID(value)

This translator can be used when defining columns

.. code-block:: python

    import uuid 
    from cerami.decorators import primary_key
    from cerami.datatype import String

    @primary_key('uuid')
    class MyModel(db.Model):
        uuid = String(Translator_cls=UUID4Translator, default = uuid.uuid4)
        name = String()

Every column takes in a `translator_cls` kwarg to set the translator object used. If we wanted to, we could create our own datatype that defaults to this translator so it is easier to reproduce.

.. code-block:: python

    from cerami.datatype import String

    class UUID4(String):
        def __init__(self, translator_cls=UUID4Translator, default=None, column_name=""):
            super(UUID4, self).__init__(
                translator_cls=translator_cls,
                default=default,
                column_name=column_name)

.. code-block:: python

    @primary_key('uuid')
    class MyModel(db.Model):
        uuid = UUID4(default=uuid.uuid4)
        name = String()

Email Address Example
---------------------
If we are building some sort of web application that stores a user's email address in the database, we want to make sure that they are saved in all lower case and without any leading or trailing spaces. Otherwise, logging in may be difficult if the user does not match the exact letter casing used when creating the account.

We can create a custom translator class which does this for us.

.. code-block:: python

    from cerami.datatype.translator import BaseDatatypeTranslator

    class EmailTranslator(BaseDatatypeTranslator):
        """Automatically remove whitespace and make string lowercase

        We do not need to override the `format_for_cerami()` method because by default it will return the data as-is (already in the correct format)
        """
        def format_for_dynamodb(self, value):
            return value.lower().strip();

.. code-block:: python

    from cerami.decorators import primary_key
    from cerami.datatype import String

    @primary_key('email')
    class User(db.Model):
        email = String(translator_cls=EmailTranslator)
        name = StrTranslator
