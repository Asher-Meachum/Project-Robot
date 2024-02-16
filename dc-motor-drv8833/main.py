'''
Full speed - car.change_speed(100)
Half speed - car.change_speed(50)
No speed - car.change_speed(0)
'''

from robot_car import RobotCar
from machine import Pin
from time import sleep
from rp2 import bootsel_button

# Other GPIO Pins
SLEEP = Pin(15, Pin.OUT) # This allows the DRV8833 to be turned on.
LED = Pin("LED", Pin.OUT) # When not connected to a computer or display, we can use this to know when the code starts, when it ends, and at what point we are in the code.

def initilization():
    motor_pins = [16, 17, 18, 19]
    SLEEP.value(1) # Turns pin 15 to high.
    LED.value(1) # Turns the onboard LED on.
    car = RobotCar(motor_pins, 20000) # Create an instance of our robot car

def deinitialization():
    SLEEP.value(0)
    LED.value(0)
    car.deinit()

def n():
    car.forward()
    sleep(1.15)

def s():
    car.back()
    sleep(1.15)

def w():
    car.left()
    sleep(0.38)

def e():
    car.right()
    sleep(0.38)

try:
    initialization()
    if bootsel_button():

        deinitialization()

except KeyboardInterrupt:
    deinitialization()
