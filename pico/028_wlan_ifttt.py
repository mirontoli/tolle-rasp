'''
This is for connecting to wifi and notifying through IFTTT mobile app
For this to work, you need to set up an IFTTT applet "if webhook then push notification"

secrets inspired by https://github.com/pi3g/pico-w/blob/main/MicroPython/I%20Pico%20W%20LED%20web%20server/main.py
'''
import time
from secrets import secrets
import network
import urequests

# save secrets.py on raspberry pi pico
#secrets = {
#    'ssid': 'your ssid',
#    'password': 'password'
#    'webhook': 'https://...'
#}

ssid = secrets['ssid']
password = secrets['password']
webhook = secrets['webhook'] #ifttt webhook

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print(wlan.status()) # first status 1 not connected

max_wait = 10
while max_wait > 0:
    if wlan.status() == 3:
        break
    max_wait -= 1
    print('connecting')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Pico is now connected to WLAN')
    
r = urequests.get(webhook)
print(r.content)
r.close()

