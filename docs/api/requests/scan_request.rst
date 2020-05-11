ScanRequest
===========

A ``ScanRequest`` is used to perform a ``scan`` transaction with DynamoDB. It is used for retrieving one or many items. Scanning can filter by any attributes, but it is far slower than a ``query``.

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html

.. autoclass:: cerami.request.ScanRequest
    :members:
    :inherited-members:
    :no-undoc-members:
