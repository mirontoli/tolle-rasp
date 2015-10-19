#!/usr/bin/env python3
"""
 sends temperature to slack
 invoke this from command line:
 sudo python3 send_temp.py
 replace <token> with your slack token
"""

from sense_hat import SenseHat
import os
import time

__author__ = "Anatoly Mironov @mirontoli, David Stenzelius "

sense = SenseHat()

while True:
    os.system('curl -X POST --data-urlencode \'payload={"text": "Temperature %s greetings from *monkey-bot*.", "channel": "#random", "username": "monkey-bot", "icon_emoji": ":monkey_face:"}\' https://hooks.slack.com/services/<token>' % sense.temp)
    time.sleep(20)