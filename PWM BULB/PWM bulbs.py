from machine import Pin, PWM
pwm=PWM(Pin(1))
pwm.freq(1000)
from utime import sleep
while True:
    pwm.duty_u16(25000)
    