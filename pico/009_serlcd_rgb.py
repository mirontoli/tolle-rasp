# finally found how to change the backlight color
# https://diyodemag.com/projects/playing_with_raspberry_pi_pico_review_project
import machine
import utime
sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
utime.sleep(1)
i2c.writeto(114, '\x7C') # | enter settings mode

i2c.writeto(114, '\x2B') # + change color
i2c.writeto(114, '\xFF') # red
i2c.writeto(114, '\xFF') # green
i2c.writeto(114, '\xFF') # blue

i2c.writeto(114, '\x7C') # enter settings mode
i2c.writeto(114, '\x2D') # clear display
# i2c.writeto(114, '\x2C') # firmware version 1.4
i2c.writeto(114, 'Salam tence!')


