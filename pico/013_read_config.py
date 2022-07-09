import json
# save config.json on raspberry pi pico
# {"ssid":"Network","password":"Password"}
f = open('config.json', 'r')
s = f.read()
c = json.loads(s)
ssid = c['ssid']
password = c['password']
print(f'SSID: {ssid}, password: {password}')