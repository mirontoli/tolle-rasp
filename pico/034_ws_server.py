# import logging
import uasyncio
from uasyncio.websocket.server import WSReader, WSWriter

import network
from time import sleep
from secrets import secrets
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'], secrets['password'])
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


def echo(reader, writer):
    # Consume GET line
    yield from reader.readline()

    reader = yield from WSReader(reader, writer)
    writer = WSWriter(reader, writer)

    while 1:
        l = yield from reader.readline()
        print(l)
        if l == b"\r":
            await writer.awrite(b"\r\n")
        else:
            await writer.awrite(l)


# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG)
loop = uasyncio.get_event_loop()
loop.create_task(uasyncio.start_server(echo, "192.168.3.46", 8081))
loop.run_forever()
loop.close()
