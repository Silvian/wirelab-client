"""Wirelab Client Main App."""
import boto3
import json

from time import sleep

import settings

from utils.config import Config
from controllers import raspberrypi


def sqs_client():
    """Create SQS client"""
    sqs = boto3.client(
        'sqs',
        region_name=settings.AWS_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    return sqs


def process_sqs_message(sqs):
    """Receive message from SQS queue"""
    response = sqs.receive_message(
        QueueUrl=settings.AWS_QUEUE,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=20
    )

    if "Messages" in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        message_body = json.loads(message["Body"])

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=settings.AWS_QUEUE,
            ReceiptHandle=receipt_handle
        )

        return message_body


def main():
    sqs = sqs_client()
    config_file = Config()

    while True:
        message = process_sqs_message(sqs)
        config = config_file.load()
        devices = config.get("devices")

        for device in devices:
            if device["id"] == message.get("device_id"):
                switch = device["switch"]
                if switch == 1:
                    raspberrypi.switch_one(message.get("state"))
                elif switch == 2:
                    raspberrypi.switch_two(message.get("state"))
                elif switch == 3:
                    raspberrypi.switch_three(message.get("state"))
                elif switch == 4:
                    raspberrypi.switch_four(message.get("state"))

        sleep(1)


if __name__ == "__main__":
    main()
