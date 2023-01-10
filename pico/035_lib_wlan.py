'''
a lib for connecting to wlan
save it to pico as tolle_wlan.py

save also secrets.py on raspberry pi pico
secrets = {
    'ssid': 'your ssid',
    'password': 'password'
    'webhook': 'https://...'
}
'''
import network
from time import sleep
from secrets import secrets


def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['ssid'], secrets['password'])

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    max_wait = 10
    while max_wait > 0:
        if wlan.status() == 3:
            break
        max_wait -= 1
        sleep(1)

    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('Pico is connected to WLAN')
        ip = wlan.ifconfig()[0]
        print('IP: ', ip)
