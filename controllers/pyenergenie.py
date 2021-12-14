from asyncio import sleep

import settings

from controllers.constants import ON, OFF
from pyenergenie import energenie
from utils.handlers import ServiceAvailability

# service setup
service = ServiceAvailability()


async def switch_device(switch, unique_id, device_type, state, delay=0):
    if delay:
        await sleep(delay * 60)

    # get device
    energenie.init()

    if device_type == "MIHO002":
        device = energenie.Devices.MIHO002((settings.HOUSE_CODE, switch))

    else:
        # default to the legacy device
        device = energenie.Devices.MIHO008((settings.HOUSE_CODE, switch))

    if state == ON:
        await sleep(0.5)
        device.turn_on()
        await sleep(0.5)
        device.turn_on()
        await sleep(0.5)
        device.turn_on()
        # Call back and update state
        service.status_update(unique_id, state=ON)

    elif state == OFF:
        await sleep(0.5)
        device.turn_off()
        await sleep(0.5)
        device.turn_off()
        await sleep(0.5)
        device.turn_off()
        # Call back and update state
        service.status_update(unique_id, state=OFF)

    energenie.finished()
    energenie.cleanup()
