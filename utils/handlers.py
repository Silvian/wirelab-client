import signal

import requests

import settings


class DeviceCatalogue:
    """Device availability catalogue."""

    def __init__(
        self,
        devices_url=settings.DEVICES_URL,
        devices_key=settings.DEVICES_KEY,
    ):
        self.devices_url = devices_url
        self.devices_key = devices_key

    def list_devices(self):
        response = requests.get(
            url=self.devices_url,
            headers={
                'Content-Type': 'application/json',
                'X-API-KEY': self.devices_key,
            },
        ).json()

        return response


class ServiceCheck:
    """Service check status update."""

    def __init__(
        self,
        status_url=settings.STATUS_URL,
        status_key=settings.STATUS_KEY,
    ):
        self.status_url = status_url
        self.status_key = status_key

    def status_update(self, device_id, state):
        response = requests.post(
            url=self.status_url,
            headers={
                'Content-Type': 'application/json',
                'X-API-KEY': self.status_key,
            },
            json={
                'device_id': device_id,
                'state': state,
            }
        ).json()

        return response


class SignalHandler:
    kill = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill = True
