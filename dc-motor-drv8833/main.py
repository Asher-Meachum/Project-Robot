import gc
from machine import Pin
from rp2 import bootsel_button
from time import sleep
import backend as lib

# This makes sure automatic garbage collection doesn't mess up timing.
gc.disable()

# For program start confirmation when not at a display.
LED = Pin("LED", Pin.OUT)
LED.value(1)

def deinit():
    LED.value(0)
    lib.deinit()
    gc.collect()

try:
    while True:
        if bootsel_button():
            gc.collect()
            sleep(1)

            deinit()
            break

except KeyboardInterrupt:
    deinit()
