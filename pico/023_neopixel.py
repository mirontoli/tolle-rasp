# trying out 8 pixel neopixel
# https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html
# https://makersportal.com/blog/ws2812-ring-light-with-raspberry-pi-pico
from neopixel import NeoPixel
from machine import Pin
from time import sleep
np = NeoPixel(Pin(20), 8)
np[0] = (255, 0, 0)
np.write()
sleep(1)
np[0] = (0, 0, 0)
np.write()
