from machine import Pin,PWM,I2C,SPI
import ahtx0
from ssd1306 import SSD1306_SPI
import framebuf
from time import sleep
import utime


sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, scl=scl, sda=sda)
ok =Pin(10,Pin.OUT)
pourwater =Pin(21,Pin.OUT)
servo =PWM(Pin(2))
servo.freq(50)
spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))

sensor = ahtx0.AHT10(i2c)


def motion(angle):
    value =(6550/180)*angle + 1638
    print(int(value))
    return int(value)
<<<<<<< HEAD
    
while True:
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    
    
    if humidity <= 55:
=======
while True:
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    print("Temperature: ", temperature, "C")
    print("Humidity: ", humidity, "%")
    print()
    utime.sleep(1)
    if sensor.relative_humidity <= 60:
>>>>>>> 64351eb667528cfcaef4657f99c04998532e2f44
        servo.duty_u16(motion(140))
        pourwater.on()
        utime.sleep(1)
        pourwater.off()
<<<<<<< HEAD
        oled.text("Add Water!!", 10, 20)
        oled.show()
        sleep(0.5)
=======
>>>>>>> 64351eb667528cfcaef4657f99c04998532e2f44
    else:
        servo.duty_u16(motion(60))
        ok.on()
        utime.sleep(1)
        ok.off()
<<<<<<< HEAD
        oled.text("No Water Needed", 10, 20)
        oled.show()
        sleep(0.5)
        
    oled.fill(0)
    oled.text("Temp = " + str(round(temperature, 2)), 0, 0)
    oled.text("Humid = " + str(round(humidity, 2)) + "%", 0, 10)
    oled.show()
    
    utime.sleep(0.5)

