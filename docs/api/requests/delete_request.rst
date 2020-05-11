DeleteRequest
=============

A ``DeleteRequest`` is used to perform a ``delete_item`` transaction with DynamoDB. It is used for deletting a single record by its primary key. The entire primary key must be provided (including the sort key if it is defined on the table)

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html

.. autoclass:: cerami.request.DeleteRequest
    :members:
    :inherited-members:
    :no-undoc-members:
