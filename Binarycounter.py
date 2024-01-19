from machine import Pin
from utime import sleep

red1 =Pin(0,Pin.OUT)
red2 =Pin(16,Pin.OUT)
red3 =Pin(18,Pin.OUT)

sleep(2)
red1.on()
sleep(2)
red1.off()
red2.on()
sleep(2)
red2.off()
sleep(2)
red3.on()
sleep(2)
red2.on()
red1.on()
sleep(2)
red1.off()
red2.off()
red3.off()

        
    
