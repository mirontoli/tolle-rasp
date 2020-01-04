#!/usr/bin/env python

"""
 shows a creeper on sense when shaken
"""

__author__ = "Anatoly Mironov @mirontoli"



from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

g = (0, 255, 0) #Green
b = (0, 0, 0) # Black

creeper = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
    ]

creeper_left = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, b, b, g, g, b, b,
    g, g, b, b, g, g, b, b,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
    ]

creeper_right = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    b, b, g, g, b, b, g, g,
    b, b, g, g, b, b, g, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
    ]

def move():
    for i in range(3):
        sense.set_pixels(creeper)
        time.sleep(0.5)
        sense.set_pixels(creeper_left)
        time.sleep(0.5)
        sense.set_pixels(creeper)
        time.sleep(0.5)
        sense.set_pixels(creeper_right)
        time.sleep(0.5)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = round(abs(acceleration['x']), 0)
    y = round(abs(acceleration['y']), 0)
    z = round(abs(acceleration['z']), 0)

    print(x,y,z)

    if x > 1 or y > 1 or z > 1:
        move()
        #sense.set_pixels(creeper)
    else:
        sense.clear()
    time.sleep(0.1)