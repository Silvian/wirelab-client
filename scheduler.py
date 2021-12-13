import asyncio

from controllers import pyenergenie
from controllers.constants import ON
from utils.config import Config
from utils.handlers import ServiceAvailability


async def main():
    config_file = Config()
    config = config_file.load()
    devices = config.get("devices")
    service = ServiceAvailability()
    active_devices = service.list_active_devices()

    for active_device in active_devices:
        if active_device.get("auto"):
            for device in devices:
                if device["id"] == active_device.get("unique_id"):
                    await asyncio.create_task(
                        pyenergenie.switch_device(
                            switch=device["switch"],
                            unique_id=device["id"],
                            state=ON,
                            delay=active_device.get("delay"),
                        )
                    )


if __name__ == "__main__":
    asyncio.run(main())
