from machine import Pin, SPI, SoftSPI, I2C, SoftI2C
# ssd1306.py download from:
# https://raw.githubusercontent.com/micropython/micropython/master/drivers/display/ssd1306.py
import ssd1306

def get_display():
    # assign IIC or SPI
    useSPI = True
    # assign hardware SPI/IIC or software SPI/IIC
    useSoft = False
    if useSPI:
        dc = Pin(4)    # data/command
        rst = Pin(5)   # reset
        cs = Pin(15)   # chip select, some modules do not have a pin for this
        if useSoft:
            spi = SoftSPI(baudrate=500000, polarity=1, phase=0,
                          sck=Pin(14), mosi=Pin(13), miso=Pin(12))
        else:
            spi = SPI(1)  # sck=14 (scl), mosi=13 (sda), miso=12 (unused)
        display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)
    else:
        if useSoft:
            i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
        else:
            # I2C(0, scl=22, sda=21, freq=400000)
            # I2C(1, scl=25, sda=26, freq=400000)
            i2c = I2C(0)
        # using default address 0x3C
        display = ssd1306.SSD1306_I2C(128, 64, i2c)
        #display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)
    return display
