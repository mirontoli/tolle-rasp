'''
This is for connecting to wifi and notifying through IFTTT mobile app
For this to work, you need to set up an IFTTT applet "if webhook then push notification"
'''
import json
import network

# save config.json on raspberry pi pico
# {"ssid":"Network","password":"Password", "webhook":"https://..."}
f = open('config.json', 'r')
s = f.read()
c = json.loads(s)
ssid = c['ssid']
password = c['password']
webhook = c['webhook'] #ifttt webhook


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print(wlan.status()) # first status 1 not connected

import time
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
    
import urequests
r = urequests.get(webhook)
print(r.content)
r.close()

