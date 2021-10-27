import asyncio

from controllers import raspberrypi
from controllers.constants import ON
from utils.config import Config
from utils.init import ServiceAvailability


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
                    switch = device["switch"]
                    if switch == 1:
                        asyncio.create_task(
                            raspberrypi.switch_one(device["id"], ON, delay=active_device.get("delay"))
                        )
                    elif switch == 2:
                        asyncio.create_task(
                            raspberrypi.switch_two(device["id"], ON, delay=active_device.get("delay"))
                        )
                    elif switch == 3:
                        asyncio.create_task(
                            raspberrypi.switch_three(device["id"], ON, delay=active_device.get("delay"))
                        )
                    elif switch == 4:
                        asyncio.create_task(
                            raspberrypi.switch_four(device["id"], ON, delay=active_device.get("delay"))
                        )


if __name__ == "__main__":
    asyncio.run(main())
