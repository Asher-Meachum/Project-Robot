import backend as lib
from machine import Pin
from time import sleep
from rp2 import bootsel_button

LED = Pin("LED", Pin.OUT) # When not connected to a computer or display, we can use this to know when the code starts, when it ends, and at what point we are in the code.
LED.value(1) # Turns the onboard LED on.

def deinit():
    LED.value(0)
    lib.deinit()

try:
    while True:
        if bootsel_button():

            deinit()
            break

except KeyboardInterrupt:
    deinit()
