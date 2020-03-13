## Using dorm
```
# Setup the db singleton
import boto3
from dorm import Dynamo
dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000")
db = Dynamo(dynamodb)


# create classes
import uuid
from dorm.datatype import String, Set, Datetime
from dorm.decorators import primary_key

@primary_key('_id', 'title')
class Book(db.Model):
    __tablename__ = "Books"

    _id = String(default=uuid.uuid4)
    title = String()
    authors = Set(String())
    publisher = String()
    book_producer = String()
    tags = Set(String())
    published = Datetime()
    rights = String()
    identifiers = String()
    comments = String()

# Query
Book.scan\
    .filter(Book.Schema.title.eq("Zac's First Book"))\
    .filter(Book.Schema.book_producer.eq("Zac's Producer"))\
    .execute()

Book.query\
    .key_condition(Book.Schema._id.eq("XXX"))\
    .filter(Book.Schema.book_producer.eq("YYY"))\
    .execute()

Book.get\
    .key(Book.Schema._id.eq("XXX"))\
    .key(Book.Schema.title.eq("ZZZ"))\
    .execute()
```

## Setup Dynamodb / boto3
First set up your virtualenv and install `reqs.txt`

You need to install the aws2 cli and have dynamo db running locally. Dynamodb requires java to run locally as well so good luck if you dont have it. Try these steps first and see how it goes.

### Download DynamoDB Locally
1. [Download DynamoDB Locally](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
1. Unzip/Untar the content
1. Move to somewhere you wont lose it.

### Download the AWS2 CLI
1. [Download the AWS2 CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
1. Follow the install instructions

### Configure the AWS2 CLI
In order to run DynamoDB locally, you need to configure the cli as such:

```
aws2 configure
```

```
AWS Access Key ID: "fakeMyKeyId"
AWS Secret Access Key: "fakeSecretAccessKey"
us-west-1
```

### Starting DynamoDB Locally
```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

