import json
import boto3
import time
import datetime

REGION = "us-east-1"
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table('PhotoGallery')

def lambda_handler(event, context):
    photoID = event['pathParameters']['id']
    username = event['body-json']['username']
    title = event['body-json']['title']
    description = event['body-json']['description']
    tags = event['body-json']['tags']
    uploadedFileURL = event['body-json']['uploadedFileURL']

    table.update_item(
        Key={
            "PhotoID": photoID
        },
        UpdateExpression="set Username = :username, Title = :title, Description = :description, Tags = :tags, URL = :uploadedFileURL",
        ExpressionAttributeValues={
            ":username": username,
            ":title": title,
            ":description": description,
            ":tags": tags,
            ":uploadedFileURL": uploadedFileURL
        },
        ReturnValues="UPDATED_NEW"
    )

    response = {
        "statusCode": 200,
        "body": json.dumps("Photo metadata updated with ID: " + photoID)
    }

    return response