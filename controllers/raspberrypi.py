import RPi.GPIO as GPIO

from asyncio import create_task, sleep

from controllers.constants import ON, OFF
from utils.init import ServiceAvailability

# set the pins numbering mode
GPIO.setmode(GPIO.BOARD)

# Select the GPIO pins used for the encoder K0-K3 data inputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Select the signal to select ASK/FSK
GPIO.setup(18, GPIO.OUT)

# Select the signal used to enable/disable the modulator
GPIO.setup(22, GPIO.OUT)

# Disable the modulator by setting CE pin lo
GPIO.output(22, False)

# Set the modulator to ASK for On Off Keying
# by setting MODSEL pin lo
GPIO.output(18, False)

# Initialise K0-K3 inputs of the encoder to 0000
GPIO.output(11, False)
GPIO.output(15, False)
GPIO.output(16, False)
GPIO.output(13, False)

# The On/Off code pairs correspond to the hand controller codes.
# True = '1', False ='0'

# service setup
service = ServiceAvailability()


async def select_switch(switch, unique_id, state, delay=0):
    if switch == 1:
        await create_task(
            switch_one(unique_id, state, delay)
        )
    elif switch == 2:
        await create_task(
            switch_two(unique_id, state, delay)
        )
    elif switch == 3:
        await create_task(
            switch_three(unique_id, state, delay)
        )
    elif switch == 4:
        await create_task(
            switch_four(unique_id, state, delay)
        )


async def switch_one(unique_id, state, delay):
    if delay:
        await sleep(delay * 60)

    if state == ON:
        # Set K0-K3
        print("sending code 1111 socket 1 on")
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, True)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=ON)

    elif state == OFF:
        # Set K0-K3
        print("sending code 0111 Socket 1 off")
        GPIO.output(11, True)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, False)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=OFF)


async def switch_two(unique_id, state, delay):
    if delay:
        await sleep(delay * 60)

    if state == ON:
        # Set K0-K3
        print("sending code 1110 socket 2 on")
        GPIO.output(11, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, True)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=ON)

    elif state == OFF:
        # Set K0-K3
        print("sending code 0110 socket 2 off")
        GPIO.output(11, False)
        GPIO.output(15, True)
        GPIO.output(16, True)
        GPIO.output(13, False)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=OFF)


async def switch_three(unique_id, state, delay):
    if delay:
        await sleep(delay * 60)

    if state == ON:
        # Set K0-K3
        print("sending code 1101 socket 3 on")
        GPIO.output(11, True)
        GPIO.output(15, False)
        GPIO.output(16, True)
        GPIO.output(13, True)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=ON)

    elif state == OFF:
        # Set K0-K3
        print("sending code 0101 socket 3 off")
        GPIO.output(11, True)
        GPIO.output(15, False)
        GPIO.output(16, True)
        GPIO.output(13, False)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=OFF)


async def switch_four(unique_id, state, delay):
    if delay:
        await sleep(delay * 60)

    if state == ON:
        # Set K0-K3
        print("sending code 1100 socket 4 on")
        GPIO.output(11, False)
        GPIO.output(15, False)
        GPIO.output(16, True)
        GPIO.output(13, True)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=ON)

    elif state == OFF:
        # Set K0-K3
        print("sending code 0100 socket 4 off")
        GPIO.output(11, False)
        GPIO.output(15, False)
        GPIO.output(16, True)
        GPIO.output(13, False)
        # let it settle, encoder requires this
        await sleep(0.1)
        # Enable the modulator
        GPIO.output(22, True)
        # keep enabled for a period
        await sleep(0.25)
        # Disable the modulator
        GPIO.output(22, False)
        # Call back and update state
        service.status_update(unique_id, state=OFF)
