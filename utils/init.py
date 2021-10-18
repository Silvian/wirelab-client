import requests

import settings


class ServiceAvailability:
    """Service availability status update."""

    def __init__(
        self,
        webhook_url=settings.WEBHOOK_URL,
        webhook_key=settings.WEBHOOK_KEY,
    ):
        self.webhook_url = webhook_url
        self.webhook_key = webhook_key

    def status_update(self, unique_id, active):
        response = requests.post(
            url=self.webhook_url,
            headers={
                'Content-Type': 'application/json',
                'X-API-KEY': self.webhook_key,
            },
            json={
                'unique_id': unique_id,
                'active': active,
            }
        ).json()

        return response
