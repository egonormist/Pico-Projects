from machine import Pin,ADC,PWM
from utime import sleep
adc =ADC(Pin(28))
pwm =PWM(Pin(0))
pwm.freq(1000)
while True:
    pwm.duty_u16(adc.read_u16())
    
