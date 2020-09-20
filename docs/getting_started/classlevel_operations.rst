Classlevel Operations
=====================

Every model comes with several class-level methods to simplify the process of generating requests to DynamoDB.

GetItem
-------
Please see the :doc:`GetRequest <../api/requests/get_request>` api for its full usage.

.. code-block:: python

    person = Person.get.key(Person.email == 'test@test.com').execute().item

Query
-----
Please see the :doc:`QueryRequest <../api/requests/query_request>` api for its full usage.

.. code-block:: python

    response = Person.query.key(Person.email == "test@test.com").execute()
    for person in response.items:
        person.as_item()

Scan
----
Please see the :doc:`ScanRequest <../api/requests/scan_request>` api for its full usage.

.. code-block:: python

    response = Person.scan.filter(Person.name == "Mom").execute()
    for person in response.items:
        person.as_item()

PutItem
-------
Please see the :doc:`PutRequest <../api/requests/put_request>` api for its full usage.

.. code-block:: python

    Person.put.item({"email": {"S": "test@test.com"}}).execute()


UpdateItem
----------
Please see the :doc:`UpdateRequest <../api/requests/update_request>` api for its full usage.

.. code-block:: python

    Person.update \
        .key(Person.email == 'test@test.com') \
        .set(Person.name, 'Mommy') \
        .execute()

DeleteItem
----------
Please see the :doc:`DeleteItem <../api/requests/delete_request>` api for its full usage.

.. code-block:: python

    Person.delete.key(Person == 'test@test.com').execute()
