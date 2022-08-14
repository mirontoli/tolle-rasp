# finally found how to change the backlight color
# https://diyodemag.com/projects/playing_with_raspberry_pi_pico_review_project
import machine
from time import sleep
sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
sleep(0.1)
i2c.writeto(114, '\x7C') # | enter settings mode
sleep(.5)
i2c.writeto(114, '\x2B') # + change color
sleep(.1)
# next we define the colors, FF FF FF = white
# 00 00 00 is "black" more dark, no color, the text will still be black
i2c.writeto(114, '\xFF') # red value
sleep(.1)
i2c.writeto(114, '\xFF') # green value
sleep(0.1)
i2c.writeto(114, '\xFF') # blue value
sleep(.1)
i2c.writeto(114, '\x7C') # enter settings mode
sleep(.1)
i2c.writeto(114, '\x2D') # clear display
sleep(.1)
#i2c.writeto(114, '\x2C') # firmware version 1.4
i2c.writeto(114, '\rSalam tence!')
sleep(.1)
i2c.writeto(114, '\rHello world!')


