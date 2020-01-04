#!/usr/bin/env python3
"""
 2020-01-04
 displays a random joke from https://icanhazdadjoke.com/
 when the joystick is pressed in the middle
 __author__ = "Anatoly Mironov @mirontoli"
 
"""

import urllib.request
from sense_hat import SenseHat, ACTION_RELEASED

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

headers = {
    'Accept': 'text/plain',
    'User-Agent': 'tolle-rasp (https://github.com/mirontoli/tolle-rasp)' #if not provided you'll get 403 Forbidden
    }

url = 'https://icanhazdadjoke.com/'
request = urllib.request.Request(url, headers=headers)

def fetch_random_joke():
    resp = urllib.request.urlopen(request)
    contents = resp.read().decode('UTF-8') # if not decoded the text is prepended with b'
    return contents

def display_joke(joke):
    print(joke)
    sense.show_message(joke, text_colour=[0,255,0], scroll_speed=0.1)
    sense.clear()

def pressed_middle(event):
    if event.action == ACTION_RELEASED: #if not checked, it will run twice: ACTION_PRESSED and ACTION_RELEASED
        joke = fetch_random_joke()
        display_joke(joke)
    
sense.stick.direction_middle = pressed_middle
