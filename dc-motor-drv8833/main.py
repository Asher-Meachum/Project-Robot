from robot_car import RobotCar
from machine import Pin
import time

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
robot_car = RobotCar(motor_pins, 20000)

if __name__ == '__main__':
    try:
        '''
        robot_car.forward()
        robot_car.back()
        robot_car.stop()
        robot_car.left()
        robot_car.right()
        
        robot_car.change_speed(100); # Changes speed to 100%
        robot_car.forward()
            
        robot_car.change_speed(50); # Changes speed to 50%
        robot_car.forward()
            
        robot_car.change_speed(20); # Changes speed to 20%
        robot_car.forward()
            
        robot_car.change_speed(0); #Changes speed to 0%
        robot_car.forward()     
        '''
        SLEEP.value(0)
        LED.value(0)
        robot_car.deinit()

    except KeyboardInterrupt:
        SLEEP.value(0)
        LED.value(0)
        robot_car.deinit()
