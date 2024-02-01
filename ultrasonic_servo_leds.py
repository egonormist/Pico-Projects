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
   utime.sleep_us(1)
   trigger.high()
   utime.sleep_us(1)
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
       utime.sleep(1)
       stop.off()
       servo.duty_u16(motion(30))
       utime.sleep(1)
    
   else:
       go.on()
       utime.sleep(1)
       go.off()
       utime.sleep(1)
       servo.duty_u16(motion(160))
       utime.sleep(1)
   print("The distance from object is ",distance,"cm")

def motion(angle):
    writevalue=(6554/180)*angle + 1638
    print(int(writevalue))
    return int(writevalue)
    
   
while True:
   ultra()
   utime.sleep(1)