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
table_service.create_table(table_name, False)

while True:
  date = datetime.now()
  iso_date = date.isoformat()
  temp = "{0:.2f}".format(sense.temp)
  humidity = "{0:.2f}".format(sense.humidity)
  pressure = "{0:.2f}".format(sense.pressure)
  entry = {'PartitionKey': 'climate', 'RowKey': iso_date, 'Temperature': temp, 'Humidity':humidity, 'Pressure':pressure}
  table_service.insert_entity(table_name, entry)
  time.sleep(60) # wait one minute