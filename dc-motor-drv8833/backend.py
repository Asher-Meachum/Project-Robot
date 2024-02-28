from machine import PWM
from machine import Pin
from time import sleep
import gc

gc.disable() # This disables automatic garbage collection, making sure it isn't interfering with timing.

slp = Pin(15, Pin.OUT)
a1 = PWM(Pin(17))
a2 = PWM(Pin(16))
b1 = PWM(Pin(19))
b2 = PWM(Pin(18))

slp.value(1)
a1.freq(1000)
a1.duty_u16(0)
a2.freq(1000)
a2.duty_u16(0)
b1.freq(1000)
b1.duty_u16(0)
b2.freq(1000)
b2.duty_u16(0)

def stop():
    a1.duty_u16(0)
    a2.duty_u16(0)
    b1.duty_u16(0)
    b2.duty_u16(0)
    sleep(1)

def func_clean():
    stop()
    gc.collect()

def south():
    pwm_val = 0
    while pwm_val < 65535:
        pwm_val+= 2048
        if pwm_val == 63488:
            pwm_val-= 1
        a1.duty_u16(pwm_val)
        b1.duty_u16(pwm_val)
        sleep(.1)
    sleep(.5)
    func_clean()
    

def north():
    pwm_val = 0
    while pwm_val < 65535:
        pwm_val+= 2048
        if pwm_val == 63488:
            pwm_val-= 1
        a2.duty_u16(pwm_val)
        b2.duty_u16(pwm_val)
        sleep(.1)
    sleep(.5)
    func_clean()

def west():
    pwm_val = 0
    while pwm_val < 65535:
        pwm_val+= 2048
        if pwm_val == 63488:
            pwm_val-= 1
        a2.duty_u16(pwm_val)
        b1.duty_u16(pwm_val)
        sleep(.1)
    sleep(.5)
    func_clean()

def east():
    pwm_val = 0
    while pwm_val < 65535:
        pwm_val+= 2048
        if pwm_val == 63488:
            pwm_val-= 1
        a1.duty_u16(pwm_val)
        b2.duty_u16(pwm_val)
        sleep(.1)
    sleep(.5)
    func_clean()
    
def deinit():
    a1.deinit()
    a2.deinit()
    b1.deinit()
    b2.deinit()
