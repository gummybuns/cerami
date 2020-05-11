PutRequest
==========

A ``PutRequest`` is used to perform a ``put_item`` transaction on DynamoDB. It is required that the ``Item`` attribute includes the entire primary key (including the sort key if it is defined on the table)

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html

.. autoclass:: cerami.request.PutRequest
    :members:
    :inherited-members:
    :no-undoc-members:
