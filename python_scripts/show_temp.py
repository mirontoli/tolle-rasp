#!/usr/bin/env python3
"""
 2020-01-04
 displays temperature (in Celsius) and atmospheric pressure (millibar)
 it also logs the values into weather.csv
 __author__ = "Anatoly Mironov @mirontoli"
"""

from sense_hat import SenseHat
import time
from datetime import datetime

sense = SenseHat()
sense.set_rotation(180)
green = (0, 255, 0)
log_path = 'weather.csv'


def show_smile():
    w = [150, 150, 150]
    g = [0, 255, 0]
    r = [255, 0, 0]
    e = [0, 0, 0]

    smile = [
        e,e,e,e,e,e,e,e,
        e,g,g,e,e,g,g,e,
        e,g,g,e,e,g,g,e,
        e,e,e,e,e,e,e,e,
        e,e,e,e,e,e,e,e,
        g,e,e,e,e,e,e,g,
        g,g,g,g,g,g,g,g,
        e,e,e,e,e,e,e,e
        ]
    sense.set_pixels(smile)
    time.sleep(1)
    sense.clear()

def log(temp, pressure, humidity):     
    file = open(log_path, 'a+')
    now = datetime.now()
    file.write(f'{now};{temp};{pressure}\;{humidity}n')

def display_temp():
    raw_temp = sense.temp
    temp = round(raw_temp, 1)

    raw_pressure = sense.get_pressure()
    pressure = round(raw_pressure, 1) 
    
    raw_humidity = sense.get_humidity()
    humidity = round(raw_humidity, 1)
    
    temp_hum = sense.get_temperature_from_humidity()
    temp_press = sense.get_temperature_from_pressure()
    print('Pressure, Humidity, Temp, Temp from Humidity, Temp from Pressure')
    print(f'{pressure} mbar, {humidity} %, {temp} °C, {round(temp_hum, 1)} °C, {round(temp_press, 1)} °C')
    
    show_smile()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    sense.show_message(f'{now}', text_colour=[255, 192, 203], scroll_speed=.1)
    sense.show_message(f'{temp}C', text_colour=[0, 255, 0], scroll_speed=.1)
    sense.show_message(f'{pressure}mbar', text_colour=[255, 0, 0], scroll_speed=.1)
    sense.show_message(f'{humidity}%', text_colour=[0, 0, 255], scroll_speed=.1)
    
    log(temp, pressure, humidity)

while True:
    display_temp()
    time.sleep(5)