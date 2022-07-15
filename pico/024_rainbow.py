# adapted from: 
# https://github.com/maxking/micropython/blob/master/rainbow.py
# pixels.show() -> pixels.write()
# added try finally to support interrupt (ctrl-c)
import time
from machine import Pin
from neopixel import NeoPixel

pixel_pin = Pin(20)
num_pixels = 8

pixels = NeoPixel(pixel_pin, num_pixels)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)


def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.write()
        time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(rc_index & 255)
        pixels.write()



RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

try: 
    while True:
        pixels.fill(RED)
        pixels.write()
        # Increase or decrease to change the speed of the solid color change.
        time.sleep(1)
        pixels.fill(GREEN)
        pixels.write()
        time.sleep(1)
        pixels.fill(BLUE)
        pixels.write()
        time.sleep(1)

        color_chase(RED, 0.1)  # Increase the number to slow down the color chase
        color_chase(YELLOW, 0.1)
        color_chase(GREEN, 0.1)
        color_chase(CYAN, 0.1)
        color_chase(BLUE, 0.1)
        color_chase(PURPLE, 0.1)

        rainbow_cycle(0)  # Increase the number to slow down the rainbow
finally:
    for i in range(num_pixels):
        pixels[i] = (0, 0, 0)
    pixels.write()