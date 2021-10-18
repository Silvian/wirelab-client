"""Wirelab Client Main App."""
import signal
import sys

import boto3
import json

from time import sleep
import RPi.GPIO as GPIO

import settings

from controllers import raspberrypi
from utils.config import Config
from utils.init import ServiceAvailability


def sqs_client():
    """Create SQS client"""
    sqs = boto3.client(
        'sqs',
        region_name=settings.AWS_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    return sqs


def start():
    service = ServiceAvailability()
    config_file = Config()
    for device in config_file.load().get("devices"):
        service.status_update(device["id"], True)


def stop():
    service = ServiceAvailability()
    config_file = Config()
    for device in config_file.load().get("devices"):
        service.status_update(device["id"], False)


def sigint_handler(signal, frame):
    print("Exiting gracefully...")
    stop()
    GPIO.cleanup()
    sys.exit(0)


def main():
    sqs = sqs_client()
    config_file = Config()

    while True:
        config = config_file.load()
        devices = config.get("devices")

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

            for device in devices:
                if device["id"] == message_body.get("device_id"):
                    switch = device["switch"]
                    if switch == 1:
                        raspberrypi.switch_one(message_body.get("state"))
                    elif switch == 2:
                        raspberrypi.switch_two(message_body.get("state"))
                    elif switch == 3:
                        raspberrypi.switch_three(message_body.get("state"))
                    elif switch == 4:
                        raspberrypi.switch_four(message_body.get("state"))

        sleep(1)


if __name__ == "__main__":
    try:
        start()
        main()
    except Exception:
        pass

    signal.signal(signal.SIGINT, sigint_handler)
