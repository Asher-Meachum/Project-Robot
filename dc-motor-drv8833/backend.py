from machine import PWM
from machine import Pin
from time import sleep

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

a = 65535
b = 65535

def stop():
    a1.duty_u16(0)
    a2.duty_u16(0)
    b1.duty_u16(0)
    b2.duty_u16(0)
    sleep(1)

def north():
    a1.duty_u16(a)
    b1.duty_u16(b)
    sleep(.5)
    stop()

def south():
    a2.duty_u16(a)
    b2.duty_u16(b)
    sleep(.5)
    stop()

def east():
    a2.duty_u16(a)
    b1.duty_u16(b)
    sleep(.5)
    stop()

def west():
    a1.duty_u16(a)
    b2.duty_u16(b)
    sleep(.5)
    stop()
    
def deinit():
    a1.deinit()
    a2.deinit()
    b1.deinit()
    b2.deinit()
