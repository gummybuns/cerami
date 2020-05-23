Using Models
============

Defining Models
---------------
Models are defined by extending the `db.Model` class and are comprised of many `Datatypes`. It is recommended to use the `primary_key` decorator to define the model's primary key.

.. code-block:: python

    from cerami.datatype import String, Number
    from cerami.decorators import primary_key

    @primary_key('name')
    class Person(db.Model):
        __tablename__ = "People"

        name = String()
        age = Number()
        favorite_drink = String()

        def say_hello(self):
            print(f'Hello {self.name}!')

Instantiating Models
--------------------
.. code-block:: python

    person = Person(name="Bobby Boucher", age=26, favorite_drink="water")
    person.say_hello()

Saving Records (Put / Update)
-----------------------------
DynamoDB has two different save operations. `put_item` and `update_item`.

* Put will replace the entire item (or create it if its missing)
* Update works like a patch and only overwrites fields that are part of the update

.. code-block:: python

    bobby = Person(name="Bobby Boucher", age=26, favorite_drink="water")
    bobby.put() # creates Bobby

Cerami always creates records based off of the full column set. If an attribute is missing from the object, it will be saved to the database as a `null` object using DynamoDB's syntax ``{NULL: True}``

.. code-block:: python

    billy = Person(name="Billy Madison", age=27)
    # favorite_drink will be saved as None in the database
    billy.put()

Cerami keeps track of which columns have changed and will only `update` these different values.

.. code-block:: python

    billy_again = Person(name="Billy Madison", favorite_drink="beer")
    # Even though age is initialized as None, it will not be saved in the database as such
    billy_again.update()

    billy_from_db = Person.get.key(name="Billy Madison").execute().item
    billy_from_db.as_item()
    {'name': {'S': 'Billy Madison'}, 'age': {'N': '27'}, 'favorite_drink': {'S': 'beer'}}

Deleting Models
---------------
.. code-block:: python

    billy.delete()

Viewing Model Data
------------------
DynamoDB expects its data formatted in a specific dict format. This can be done automatically with the `as_item()` method.

.. code-block:: python

    bobby = Person(name="Bobby Boucher", age=26, favorite_drink="water")

    bobby.as_item()
    {'name': {'S': 'Bobby Boucher'}, 'age': {'N': '26'}, 'favorite_drink': {'S': 'water'}} 
