from machine import Pin
import utime

trigger =Pin(0,Pin.OUT)
echo =Pin(1,Pin.IN)

def distance():
    trigger.low()
    utime.sleep_us(3)
    trigger.high()
    utime.sleep_us(3)
    trigger.low()
    
    while echo.value() ==0:
        signaloff =utime.ticks_us()
    while echo.value() ==1:
        signalon =utime.ticks_us()
    timepassed = signalon - signaloff
    distance =(timepassed * 0.0343)/2
    print ('distance imecountiwa ni',distance,'cm')

while True:
    distance()
    utime.sleep(1)
        
    
    