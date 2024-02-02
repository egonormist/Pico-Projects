from machine import Pin,PWM,I2C
import ahtx0
import utime

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, scl=scl, sda=sda)
ok =Pin(15,Pin.OUT)
pourwater =Pin(16,Pin.OUT)
servo =PWM(Pin(2))
servo.freq(50)
sensor = ahtx0.AHT10(i2c)
def motion(angle):
    value =(6550/180)*angle + 1638
    print(int(value))
    return int(value)

if sensor.relative_humidity <= 50:
    servo.duty_u16(motion(140))
else:
    servo.duty_u16(motion(0))
    
while True:
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    print("Temperature: ", temperature, "C")
    print("Humidity: ", humidity, "%")
    print()
    utime.sleep(1)
    if sensor.relative_humidity <= 50:
        servo.duty_u16(motion(140))
        pourwater.on()
        utime.sleep(1)
        pourwater.off()
    else:
        servo.duty_u16(motion(60))
        ok.on()
        utime.sleep(1)
        ok.off()
