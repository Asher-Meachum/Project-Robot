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
        # Test forward, reverse, stop, turn left and turn right
        print("*********Testing forward, reverse and loop*********")
        for i in range(2):
            print("Moving forward")
            robot_car.move_forward()
            time.sleep(2)
            print("Moving backward")
            robot_car.move_backward()
            time.sleep(2)
            print("stop")
            robot_car.stop()
            time.sleep(2)
            print("turn left")
            robot_car.turn_left()
            time.sleep(2)
            print("turn right")
            robot_car.turn_right()
            time.sleep(2)
            
        print("*********Testing speed*********")
        for i in range(2):
            print("Moving at 100% speed")
            robot_car.change_speed(100);
            robot_car.move_forward()
            time.sleep(2)
            
            print("Moving at 50% speed")
            robot_car.change_speed(50);
            robot_car.move_forward()
            time.sleep(2)
            
            print("Moving at 20% of speed")
            robot_car.change_speed(20);
            robot_car.move_forward()
            time.sleep(2)
            
            print("Moving at 0% of speed or the slowest")
            robot_car.change_speed(0);
            robot_car.move_forward()
            time.sleep(2)

        SLEEP.value(0)
        LED.value(0)
        robot_car.deinit()

    except KeyboardInterrupt:
        SLEEP.value(0)
        LED.value(0)
        robot_car.deinit()
