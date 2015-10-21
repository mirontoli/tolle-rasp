#!/usr/bin/env python3
"""
shows current wlan ip,
can be scheduled to logon: .bashrc
python3 show_wlan_ip.py
or chmod u+x show_wlan_ip.py
./show_wlan_ip.py
"""

from sense_hat import SenseHat
import os
import time

__author__ = "Anatoly Mironov @mirontoli "

sense = SenseHat()
# extract ip address: http://stackoverflow.com/a/21336517/632117
# get output from shell: http://stackoverflow.com/a/3503909/632117
address = os.popen("ifconfig wlan 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'").read().replace("\n", "")
sense.show_message(address)
time.sleep(3)
sense.show_message(address)
