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


def log(temp, pressure):     
    file = open(log_path, 'a+')
    now = datetime.now()
    file.write(f'{now};{temp};{pressure}\n')

def display_temp():
    raw_temp = sense.temp
    temp = round(raw_temp)
    print(f'Temp: {temp}')
    sense.show_message(f'{temp}', text_colour=[0, 255, 0], scroll_speed=0.2)
    raw_pressure = sense.get_pressure()
    pressure = round(raw_pressure) 
    print(f'Pressure: {pressure}')
    sense.show_message(f'{pressure}', text_colour=[255, 0, 0], scroll_speed=0.2)
    
    log(temp, pressure)
    
    temp_hum = sense.get_temperature_from_humidity()
    temp_press = sense.get_temperature_from_pressure()
    print('Temp from Humidity, Default Temp, Temp from Pressure')
    print(f'{round(temp_hum)}, {round(sense.temp)}, {round(temp_press)}')

while True:
    display_temp()
    time.sleep(2)