from machine import Pin
from utime import sleep
red = Pin(0,Pin.OUT)
amber = Pin(16,Pin.OUT)
green = Pin(2,Pin.OUT)
while True:
    green.on()
    sleep(5)
    green.off()
    amber.on()
    sleep(3)
    amber.off()
    red.on()
    sleep(5)
    amber.on()
    sleep(3)
    red.off()
    amber.off()
    