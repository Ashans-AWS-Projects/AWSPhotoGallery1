import json
import boto3  
import time
import datetime
from boto3.dynamodb.conditions import Key, Attr

REGION="us-east-1"
dynamodb = boto3.resource('dynamodb',region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID=event['params']['path']['id']

    table.delete_item(
        Key = {
            "PhotoID": photoID,
            "CreationTime": int(photoID)

        }
    )

    response = {
        "statusCode": 200,
        "body": json.dumps("Photo deleted with ID: " + photoID)
    }
    return response
