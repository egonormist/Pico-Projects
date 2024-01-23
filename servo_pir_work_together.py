from machine import Pin, PWM
from utime import sleep

servo =PWM(Pin(16))
servo.freq(50)
motion =Pin(17,Pin.IN)

def motor(prop):
    finalvalue =(6554/180)*prop + 1638
    print (int(finalvalue))
    return int(finalvalue)

def movement():
    if motion.value() ==1:
        servo.duty_u16(motor(90))
        sleep(5)
    
    else:
        servo.duty_u16(motor(0))
        sleep(1)
    
while True:
    movement()
    