import os
import boto3

session = boto3.session.Session(profile_name=os.environ["AWS_PROFILE"])
dynamodb = session.resource('dynamodb',
                            region_name='us-east-1',
                            endpoint_url="https://dynamodb.us-east-1.amazonaws.com:443")


table = dynamodb.create_table(
    TableName='Scoreboard',
    KeySchema=[
        {
            'AttributeName': 'game_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'game_date_est',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'game_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'game_date_est',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
