from machine import PWM, Pin
from time import sleep
import gc

# This makes sure automatic garbage collection doesn't interfering with timing.
gc.disable()

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
    while pwm_val > 0:
        pwm_val- = 2048
        a1.duty_u16(pwm_val)
        b1.duty_u16(pwm_val)
        if pwm_val == 2047:
            pwm_val+ = 1
        sleep(0.01)
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
     while pwm_val > 0:
        pwm_val- = 2048
        a2.duty_u16(pwm_val)
        b2.duty_u16(pwm_val)
        if pwm_val == 2047:
            pwm_val+ = 1
        sleep(0.01)
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
     while pwm_val > 0:
        pwm_val- = 2048
        a2.duty_u16(pwm_val)
        b1.duty_u16(pwm_val)
        if pwm_val == 2047:
            pwm_val+ = 1
        sleep(0.01)
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
     while pwm_val > 0:
        pwm_val- = 2048
        a1.duty_u16(pwm_val)
        b2.duty_u16(pwm_val)
        if pwm_val == 2047:
            pwm_val+ = 1
        sleep(0.01)
    func_clean()
    
def deinit():
    slp.value(0)
    a1.deinit()
    a2.deinit()
    b1.deinit()
    b2.deinit()
