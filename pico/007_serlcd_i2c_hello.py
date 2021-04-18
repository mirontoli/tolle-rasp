# page 118 of "Get started with Raspberry Pi Pico"
import machine
sda = machine.Pin(0)
scl = machine.Pin(1)
i2c = machine.I2C(0, sda=sda, scl=scl, freq=400000)
i2c.writeto(114, '\x7C')
i2c.writeto(114, '\x2D') # clear display
i2c.writeto(114, 'hello world')
# i2c.writeto(114, '\x03') # ??
# i2c.writeto(114, '\x2B', ['\xFF', ' \x00', '\x00']) # set rgb, does not work
# i2c.writeto(114, '\x2B\xFF\x00\x00') # does not work
# i2c.writeto(114, '\x2B', '\xFF', '\x00', '\x00') # does not work
# i2c.writeto(114, '\x2B', '\xFF\x00\x00') # 
# i2c.writeto(114, '\xD9') # green backlight, does not work
# i2c.writeto(114, '\x2C') # display firmware version, only shows ","
# getting error if two writeto in a row
# i2c.writeto(114, 'salam tence')
# i2c.writeto(114, 'Салам тӗнче')
# i2c.writeto(114, 'EMILIE')
# i2c.writeto(114, 'WWQÅÖMYFPOLIERNGVNBÖÄUZ')
# i2c.writeto(114, '\xDF') # should show degree sign, does not work