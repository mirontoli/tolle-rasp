# page 120 of "Get started with Raspberry Pi Pico"
# reworked
import machine
from time import sleep

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
adc = machine.ADC(4)
conversion_factor = 3.3/(65535)

while True:
    reading = adc.read_u16() * conversion_factor
    temperature = 25 - (reading - 0.706)/0.001721
    i2c.writeto(114, '\x7C')
    # must sleep here otherwise error: OSError: [Errno 5] EIO
    sleep(0.1)
    i2c.writeto(114, '\x2D')
    sleep(0.1)
    out_string = '\rTemp: ' + str(temperature)
    i2c.writeto(114, out_string)
    sleep(3)