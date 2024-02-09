'''
Forward - car.forward
Backward - car.back
Left - car.left
Right - car.right
Full speed - car.change_speed(100)
Half speed - car.change_speed(50)
No speed - car.change_speed(0)
'''
from robot_car import RobotCar
from machine import Pin
from time import sleep
# Pico W GPIO Pin
LEFT_MOTOR_PIN_1 = 16
LEFT_MOTOR_PIN_2 = 17
RIGHT_MOTOR_PIN_1 = 18
RIGHT_MOTOR_PIN_2 = 19
# Other GPIO Pins
SLEEP = Pin(15, Pin.OUT) # This allows the DRV8833 to be turned on.
LED = Pin("LED", Pin.OUT) # When not connected to a computer or display, we can use this to know when the code starts, when it ends, and at what point we are in the code.
SLEEP.value(1) # Turns pin 15 to high.
LED.value(1) # Turns the onboard LED on.
motor_pins = [LEFT_MOTOR_PIN_1, LEFT_MOTOR_PIN_2, RIGHT_MOTOR_PIN_1, RIGHT_MOTOR_PIN_2]
# Create an instance of our robot car
car = RobotCar(motor_pins, 20000)
if __name__ == '__main__':
    try:

        SLEEP.value(0)
        LED.value(0)
        car.deinit()

    except KeyboardInterrupt:
        SLEEP.value(0)
        LED.value(0)
        car.deinit()
