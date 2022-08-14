# page 120 of "Get started with Raspberry Pi Pico"
# reworked pico_temp_sensor as in 025...
import machine
from picozero import pico_temp_sensor
from time import sleep

sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)

while True:
    temperature = pico_temp_sensor.temp
    i2c.writeto(114, '\x7C')
    # must sleep here otherwise error: OSError: [Errno 5] EIO
    sleep(.1)
    i2c.writeto(114, '\x2D')
    sleep(.1)
    out_string = 'Temperature:\r\r' + '{:.2f}'.format(temperature) + ' C'
    i2c.writeto(114, out_string)
    sleep(3)