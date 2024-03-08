from machine import PWM, Pin
from time import sleep
import gc

# Prevents automatic garbage collection from interfering with timing.
gc.disable()

# This turns the DRV8833 board on. Is for Adafruit board.
slp = Pin(15, Pin.OUT)

a1 = PWM(Pin(17))
a2 = PWM(Pin(16))
b1 = PWM(Pin(19))
b2 = PWM(Pin(18))

slp.value(1)
a1.init(freq = 1000, duty_u16 = 0)
a2.init(freq = 1000, duty_u16 = 0)
b1.init(freq = 1000, duty_u16 = 0)
b2.init(freq = 1000, duty_u16 = 0)

directions = {
    "n": (a2, b2),
    "s": (a1, b1),
    "e": (a1, b2),
    "w": (a2, b1)
}


def change_speed(sof, dir):
    if sof > 0: # This part is for acceleration
        if sof < 3: # For forwards and backwards
            pwm_val = -1
            change_frac = 8192
            while pwm_val < 65535:
                pwm_val+= change_frac
                directions[dir][0].duty_u16(pwm_val)
                directions[dir][1].duty_u16(pwm_val)
                sleep(0.103)
        elif sof > 2: # For rotation
            pwm_val = -1
            change_frac = 8192
            while pwm_val < 65535:
                pwm_val+= change_frac
                directions[dir][0].duty_u16(pwm_val)
                directions[dir][1].duty_u16(pwm_val)
                sleep(0.103)
    elif sof < 0: # This part is for deceleration.
        if sof > -3: # For forwards and backwards
            pwm_val = 65535
            change_frac = 8192
            while pwm_val > 0:
                pwm_val-= change_frac
                directions[dir][0].duty_u16(pwm_val)
                directions[dir][1].duty_u16(pwm_val)
                sleep(0.103)
        elif sof < -2: # For rotation
            pwm_val = 65535
            change_frac = 8192
            while pwm_val > 0:
                pwm_val-= change_frac
                directions[dir][0].duty_u16(pwm_val)
                directions[dir][1].duty_u16(pwm_val)
                sleep(0.103)


def mov(dir):
    if dir == "n":
        change_speed(1, "n")
        change_speed(-1, "n")
        gc.collect()
    elif dir == "s":
        change_speed(1, "s")
        change_speed(-1, "s")
        gc.collect()
    elif dir == "e":
        change_speed(3, "e")
        change_speed(-3, "e")
        gc.collect()
    elif dir == "w":
        change_speed(3, "w")
        change_speed(-3, "w")
        gc.collect()


def deinit():
    slp.value(0)
    a1.deinit()
    a2.deinit()
    b1.deinit()
    b2.deinit()
