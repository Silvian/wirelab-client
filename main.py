"""Wirelab Client Main App."""
import asyncio
import sys

import boto3
import json

from asyncio import sleep

import settings

from pyenergenie import energenie
from controllers import pyenergenie
from utils.handlers import DeviceCatalogue, SignalHandler


def sqs_client():
    """Create SQS client"""
    sqs = boto3.client(
        "sqs",
        region_name=settings.AWS_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY,
    )
    return sqs


def start():
    pass


def stop():
    pass


async def main():
    sqs = sqs_client()
    device_catalogue = DeviceCatalogue()
    devices = device_catalogue.list_devices()
    handler = SignalHandler()

    while not handler.kill:
        response = sqs.receive_message(
            QueueUrl=settings.AWS_QUEUE,
            AttributeNames=[
                "SentTimestamp"
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                "All"
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=20
        )

        if "Messages" in response:
            message = response["Messages"][0]
            receipt_handle = message["ReceiptHandle"]
            message_body = json.loads(message["Body"])
            message_data = json.loads(message_body["Message"])

            # Delete received message from queue
            sqs.delete_message(
                QueueUrl=settings.AWS_QUEUE,
                ReceiptHandle=receipt_handle
            )

            for device in devices:
                if device["device_id"] == message_data.get("device_id"):
                    await asyncio.create_task(
                        pyenergenie.switch_device(
                            switch=device["switch"],
                            device_id=device["device_id"],
                            device_type=device["type"],
                            state=message_data.get("state"),
                        )
                    )

        await sleep(1)


if __name__ == "__main__":
    start()
    asyncio.run(main())
    stop()
    energenie.cleanup()
    sys.exit(0)
