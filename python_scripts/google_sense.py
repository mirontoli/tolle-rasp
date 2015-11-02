#!/usr/bin/env python

"""
 sends temperature, humidity and pressure 
 gathered from Sense Hat on Raspberry Pi2 to Google Storage
 only python works with gspread , not python3,
 pip install gspread
 pip install oauth2client
 invoke (no sudo required): python google_sense.py
 how to set up environment and get auth2 key from google:
 http://gspread.readthedocs.org/en/latest/oauth2.html
 https://github.com/JeremyMorgan/Raspberry_Pi_Weather_Station/blob/master/google.py
 you have to run worksheet.resize(1) the first time:

"""

import time
from sense_hat import SenseHat
from datetime import datetime
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

__author__ = "Anatoly Mironov @mirontoli"

sense = SenseHat()

json_key = json.load(open('Climate Data-154d73f0cb97.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
gc = gspread.authorize(credentials)
sh = gc.open("climateData")
worksheet = sh.get_worksheet(0)
a1 = worksheet.acell('A1').value
if a1 != 'Timestamp':
  worksheet.resize(1)
  worksheet.append_row(('Timestamp', 'Temperature', 'Humidity', 'Pressure'))
while True :
  sense.show_letter('S', text_colour=[0, 114, 198])
  date = datetime.now()
  iso_date = date.isoformat()    
  raw_temp = sense.temp
  #calculate temperature https://www.raspberrypi.org/forums/viewtopic.php?t=111457&p=769672
  calctemp = 0.0071 * raw_temp * raw_temp + 0.86 * raw_temp - 10.0
  temp = "{0:.2f}".format(calctemp)
  humidity = "{0:.2f}".format(sense.humidity)
  pressure = "{0:.2f}".format(sense.pressure)
  worksheet.append_row((datetime.now(), temp, humidity, pressure))
  time.sleep(2) #sleep 2 minutes, otherwise it goes to fast for the poc :)
  sense.clear()
  time.sleep(58) #clear sense
