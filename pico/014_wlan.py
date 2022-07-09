import json
# save config.json on raspberry pi pico
# {"ssid":"Network","password":"Password"}
f = open('config.json', 'r')
s = f.read()
c = json.loads(s)
ssid = c['ssid']
password = c['password']

import network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
print(wlan.status()) # first status 1 not connected

import time
max_wait = 10
while max_wait > 0:
    if wlan.status() == 3:
        print('WLAN connected')
        break
    max_wait -= 1
    print('connecting')
    time.sleep(1)
    


