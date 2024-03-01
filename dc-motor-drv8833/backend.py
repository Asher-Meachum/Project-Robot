from machine import PWM, Pin
from time import sleep
import gc

# This makes sure automatic garbage collection doesn't interfering with timing.
gc.disable()

slp = Pin(15, Pin.OUT) # This turns the DRV8833 board on. Is for Adafruit board.
a1 = PWM(Pin(17))
a2 = PWM(Pin(16))
b1 = PWM(Pin(19))
b2 = PWM(Pin(18))

slp.value(1)
a1.init(freq = 1000, duty_u16 = 0)
a2.init(freq = 1000, duty_u16 = 0)
b1.init(freq = 1000, duty_u16 = 0)
b2.init(freq = 1000, duty_u16 = 0)

def accel(adir):
    magic_num = 2048
    pwm_val = 0
    while pwm_val < 65535:
        pwm_val+= magic_num
        if pwm_val == magic_num:
            pwm_val-= 1
        if adir == "n":
            a2.duty_u16(pwm_val)
            sleep(.05)
            b2.duty_u16(pwm_val)
        elif adir == "s":
            a1.duty_u16(pwm_val)
            sleep(0.02)
            b1.duty_u16(pwm_val)
        elif adir == "e":
            a1.duty_u16(pwm_val)
            sleep(0.003)
            b2.duty_u16(pwm_val)
        elif adir == "w":
            a2.duty_u16(pwm_val)
            sleep(0.01)
            b1.duty_u16(pwm_val)
        sleep(0.1)

def deaccel(ddir):
    magic_num = 2048
    pwm_val = 65535
    while pwm_val > 0:
        pwm_val-= magic_num
        if pwm_val == magic_num:
            pwm_val-= 1
        if ddir == "n":
            a2.duty_u16(pwm_val)
            b2.duty_u16(pwm_val)
        elif ddir == "s":
            a1.duty_u16(pwm_val)
            b1.duty_u16(pwm_val)
        elif ddir == "e":
            a1.duty_u16(pwm_val)
            b2.duty_u16(pwm_val)
        elif ddir == "w":
            a2.duty_u16(pwm_val)
            b1.duty_u16(pwm_val)
        sleep(0.1)

def mov(dir):
    if dir == "n":
        accel("n")
        deaccel("n")
        gc.collect()
    elif dir == "s":
        accel("s")
        deaccel("s")
        gc.collect()
    elif dir == "e":
        accel("e")
        deaccel("e")
        gc.collect()
    elif dir == "w":
        accel("w")
        deaccel("w")
        gc.collect()
    
def deinit():
    slp.value(0)
    a1.deinit()
    a2.deinit()
    b1.deinit()
    b2.deinit()
