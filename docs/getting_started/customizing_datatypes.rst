Customizing Datatypes
=====================

While DynamoDB is limited in the datatypes it accepts, Cerami was built to easily create unique columns that can be translated back into one of the types required by DynamoDB.

All :doc:`DynamoDataType <../api/datatypes/base_datatype>` objects include a :doc:`Mapper <../api/mappers/index>` object whose purpose is to transform a models column to and from the format supported by DynamoDB. For example, DynamoDB supports numbers as columns, but these values must be converted to strings before submitted to the database. Looking at the `IntegerMapper`:

.. code-block:: python

    class IntegerMapper(BaseDatatypeMapper):
        def resolve(self, value):
            """convert the number into a string"""
            return str(value)

        def parse(self, value):
            """convert the number into an int"""
            return int(value)

The `resolve` method converts the column's number into a string before sending it to DynamoDB. The `parse` method converts the database value back into a number when receiving it from DynamoDB.

Since every Mapper defines methods to consistently convert data to and from DynamoDB, it can be leveraged to create custom data types.

Creating A UUID Datatype
------------------------
We want to store uuids in one of our tables. In order to do so, a new mapper must be created. Like in the example above, all we need to do is override the `resolve` and `parse` methods.

.. code-block:: python

    from uuid import UUID
    from cerami.datatype.mapper import BaseDatatypeMapper

    class UUID4Mapper(BaseDatatypeMapper):
        def resolve(self, value):
            """convert the uuid into a string"""
            return str(value)

        def parse(self, value):
            """convert the string back into a uuid"""
            return UUID(value)

This mapper can be used when defining columns

.. code-block:: python

    import uuid 
    from cerami.decorators import primary_key
    from cerami.datatype import String

    @primary_key('uuid')
    class MyModel(db.Model):
        uuid = String(mapper_cls=UUID4Mapper, default = uuid.uuid4)
        name = String()

Every column takes in a `mapper_cls` kwarg to set the mapper object used. If we wanted to, we could create our own datatype that defaults to this mapper so it is easier to reproduce.

.. code-block:: python

    from cerami.datatype import String

    class UUID4(String):
        def __init__(self, mapper_cls=UUID4Mapper, default=None, column_name=""):
            super(UUID4, self).__init__(
                mapper_cls=mapper_cls,
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

We can create a custom mapper class which does this for us.

.. code-block:: python

    from cerami.datatype.mapper import BaseDatatypeMapper

    class EmailMapper(BaseDatatypeMapper):
        def resolve(self, value):
            return value.lower().strip();

.. code-block:: python

    from cerami.decorators import primary_key
    from cerami.datatype import String

    @primary_key('email')
    class User(db.Model):
        email = String(mapper_cls=EmailMapper)
        name = String()

