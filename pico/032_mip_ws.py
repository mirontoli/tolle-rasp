import mip
import network
from secrets import secrets
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'], secrets['password'])
# wait
# https://forum.micropython.org/viewtopic.php?f=15&t=6568
mip.install()
mip.install("uasyncio")
mip.install("uasyncio.websocket.server")
