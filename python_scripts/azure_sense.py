#!/usr/bin/env python

"""
 sends temperature, humidity and pressure 
 gathered from Sense Hat on Raspberry Pi2 to Azure Table Storage
 only python works with Azure , not python3,
 sudo pip install azure-storage
 invoke (no sudo required): python azure_sense.py
"""

import time
from sense_hat import SenseHat
from datetime import datetime
from azure.storage.table import TableService

__author__ = "Anatoly Mironov @mirontoli"

sense = SenseHat()

table_service = TableService(account_name='tolle', account_key='ho2zakf/8rmDckS3pGOTPWwIwCzNwVJxd5hDb3R15wms2fZJG/aX53PDsTWBYsuTPwF7802IKk2QcrJ5FO7i6w==')
table_name = 'climateData'
partition_key = 'climate2'
table_service.create_table(table_name, False)

while True:
  sense.show_letter('S', text_colour=[0, 114, 198])
  date = datetime.now()
  iso_date = date.isoformat()    
  raw_temp = sense.temp
  #calculate temperature https://www.raspberrypi.org/forums/viewtopic.php?t=111457&p=769672
  calctemp = 0.0071 * raw_temp * raw_temp + 0.86 * raw_temp - 10.0
  temp = "{0:.2f}".format(calctemp)
  humidity = "{0:.2f}".format(sense.humidity)
  pressure = "{0:.2f}".format(sense.pressure)
  entry = {'PartitionKey': partition_key, 'RowKey': iso_date, 'Temperature': temp, 'Humidity':humidity, 'Pressure':pressure}
  table_service.insert_entity(table_name, entry)
  sense.clear()
  time.sleep(60) # wait one minute
