.. Cerami documentation master file, created by
   sphinx-quickstart on Sun May 10 14:49:27 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Cerami's documentation!
==================================
Cerami is a python library that hopefully provides some sanity to boto3's DynamoDB client. Its intended use is as a library to help define table data through the creation of models and create sane, readable, and reproducable DynamoDB requests.

As an example:

.. code-block:: python

    import boto3
    from cerami import Cerami
    from cerami.datatype import String
    from cerami.decorators import primary_key

    dynamodb = boto3.client('dynamodb')
    db = Cerami(dynamodb)

    # Configure a Model
    @primary_key('title')
    class Book(db.Model):
        __tablename__ = "Books"
        title = String()
        author = String()

    Book.scan.filter(Book.author.eq("Dav Pilkey")).execute()
    # Replaces
    dynamodb.scan(
        TableName="Books",
        FilterExpression="#a = :author",
        ExpressionAttributeNames={"#a": "author"},
        ExpressionAttributeValues={":author": {"S": "Dav Pilkey"}})


    Book.query.key(Book.title.eq('Captain Underpants')).execute()
    # Replaces
    dynamodb.query(
        TableName="Books"
        KeyConditionExpression="#t = :title"
        ExpressionAttributeNames={"#t": "title"}
        ExpressionAttributeValues={":title": {"S": "Captain Underpants"}})


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started/index
   api/index

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
