import asyncio

from controllers import pyenergenie
from controllers.constants import ON
from utils.handlers import DeviceCatalogue


async def main():
    device_catalogue = DeviceCatalogue()
    devices = device_catalogue.list_devices()

    for device in devices:
        if device.get("auto"):
            await asyncio.create_task(
                pyenergenie.switch_device(
                    switch=device["switch"],
                    device_id=device["device_id"],
                    device_type=device["type"],
                    state=ON,
                )
            )


if __name__ == "__main__":
    asyncio.run(main())
