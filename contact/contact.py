import boto3
import os
import json

topicArn = os.environ['TOPIC_ARN']
client = boto3.client('sns')


def lambda_handler(event, context):
    body_dict = json.loads(event['body'])
    print(body_dict)

    message = 'Contact Request:\n\n'

    if 'firstName' in body_dict:
        message += 'First name: ' + body_dict['firstName'] + "\n"
    if 'lastName' in body_dict:
        message += 'Last name: ' + body_dict['lastName'] + "\n"
    if 'company' in body_dict:
        message += 'Company: ' + body_dict['company'] + "\n"
    if 'email' in body_dict:
        message += 'Email: ' + body_dict['email'] + "\n"
    if 'message' in body_dict:
        message += 'Message: ' + body_dict['message'] + "\n"

    response = client.publish(
        TopicArn=topicArn,
        Message=message
    )

    print(response)

    return {
        "statusCode": 202
    }
