from machine import Pin
import utime

redlight =Pin(15,Pin.OUT)
sensor =Pin(0,Pin.IN)

def sensing():
    if sensor.value() ==1:
        print('MOTION!!')
        redlight.on()
        utime.sleep(2)
        
    else:
        print('NO ONE THEREf')
        redlight.off
        utime.sleep(1)

while True:
    sensing()