from robot_car import RobotCar
from machine import Pin
from time import sleep

straight_time = 1.15
turn_time = 0.38

# Pico W GPIO Pin
LEFT_MOTOR_PIN_1 = 16
LEFT_MOTOR_PIN_2 = 17
RIGHT_MOTOR_PIN_1 = 18
RIGHT_MOTOR_PIN_2 = 19

# Other GPIO Pins
SLEEP = Pin(15, Pin.OUT) # This allows the DRV8833 to be turned on.
LED = Pin("LED", Pin.OUT) # When not connected to a computer or display, we can use this to know when the code starts, when it ends, and at what point we are in the code.

motor_pins = [LEFT_MOTOR_PIN_1, LEFT_MOTOR_PIN_2, RIGHT_MOTOR_PIN_1, RIGHT_MOTOR_PIN_2]

SLEEP.value(1) # Turns pin 15 to high.
LED.value(1) # Turns the onboard LED on.
car = RobotCar(motor_pins, 20000) # Create an instance of the robot car

def north():
    car.forward()
    sleep(straight_time)

def south():
    car.back()
    sleep(straight_time)

def left():
    car.left()
    sleep(turn_time)

def right():
    car.right():
    sleep(turn_time)


if __name__ == '__main__':
    try:
        car.forward()
        sleep(0.58)
        def from_14_to_7():
            right()
            north()
            left()
            north()
            right()
            north() # Into 12 (Gate Zone)
            left()
            north()
            left()
            north()
        from_14_to_7()
        right()
        north() # Into 3 (Gate Zone)
        left()
        left()
        north()
        right()
        north()
        left()
        north()
        right()
        north() # Into 9 (Gate Zone)
        left()
        north()
        left()
        north()
        from_14_to_7()
        north()
        north()
        while i>3:
            right()
            north()
        car.stop()
        
        SLEEP.value(0)
        LED.value(0)
        car.deinit()

    except KeyboardInterrupt:
        SLEEP.value(0)
        LED.value(0)
        car.deinit()
