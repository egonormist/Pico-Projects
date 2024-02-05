from machine import Pin, SPI, I2C
from ssd1306 import SSD1306_SPI
import framebuf
from time import sleep
import utime
import ahtx0

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, scl=scl, sda=sda)

spi = SPI(0, 100000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 64, spi, Pin(17),Pin(20), Pin(16))

sensor = ahtx0.AHT10(i2c)
while True:
    temperature = round(sensor.temperature, 2)
    humidity = round(sensor.relative_humidity, 2)
    print("Temperature: ", temperature, "C")
    print("Humidity: ", humidity, "%")
    print()
    utime.sleep(1)
    try:
        for i in range(128):
            for j in range(15):
                
                oled.fill(0)
                oled.show()
                #sleep(1)
                oled.text(str(sensor.temperature),60,0)
                oled.text(str(sensor.relative_humidity),60,10)
                oled.text("Temp =",0,0)
                oled.text("Humid =",0,10)
                oled.text("%",0,10)
                oled.show()
                utime.sleep_ms(1000)
    except KeyboardInterrupt:
        break