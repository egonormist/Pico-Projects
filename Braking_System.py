#library imports

from machine import Pin,PWM
import utime

#object creation

trigger = Pin(0, Pin.OUT)
echo = Pin(1, Pin.IN)
go =Pin(15,Pin.OUT)
stop =Pin(16,Pin.OUT)
servo =PWM(Pin(2))
servo.freq(50)

def ultra():
   #setting the pulse

   trigger.low()
   trigger.high()
   trigger.low()
   
   #timestamps
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   if distance <=50:
       stop.on()
       utime.sleep(0.1)
       stop.off()
       servo.duty_u16(motion(30))
       
    
   else:
       go.on()
       utime.sleep(0.1)
       go.off()
       servo.duty_u16(motion(160))
       
   print("The distance from object is ",distance,"cm")

def motion(angle):
    value=(6554/180)*angle + 1638
    print(int(value))
    return int(value)
    
   
while True:
   ultra()
   utime.sleep(1)