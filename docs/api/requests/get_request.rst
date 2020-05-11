GetRequest
==========

A ``GetRequest`` is used to perform a ``get_item`` transaction with DynamoDB. It is used for retrieving a single item by its primary key. The entire primary key must be provided (including a sort key if it is defined on the table)

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html

.. autoclass:: cerami.request.GetRequest
    :members:
    :inherited-members:
    :no-undoc-members:
