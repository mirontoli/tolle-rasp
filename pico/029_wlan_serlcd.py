'''
This is a little server connected to serlcd as in 026
partly inspired by: https://picockpit.com/raspberry-pi/run-web-server-to-control-onboard-led-on-raspberry-pi-pico-w/
'''
from machine import Pin, I2C
from time import sleep
from secrets import secrets
import network
from socket import socket, getaddrinfo

# set up SerLCD  
sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=sda, scl=scl, freq=400000)
sleep(.1)

# output messages on serlcd
def msg_serlcd(msg, clear=True, newline=True):
    if clear: #clear screen
        i2c.writeto(114, '\x7C') # enter settings mode
        sleep(.1)
        i2c.writeto(114, '\x2D') # clear screen
        sleep(.1)
    elif newline: # new line if append
        msg = f'\r{msg}'
    i2c.writeto(114, msg)
    sleep(.1)

msg_serlcd('Starting...')
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
#print(wlan.status()) # first status 1 not connected

max_wait = 10
msg_serlcd('Connecting')
while max_wait > 0:
    if wlan.status() == 3:
        break
    max_wait -= 1
    
    sleep(1)
    msg_serlcd('.', clear=False, newline=False)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    ip = wlan.ifconfig()[0]
    msg_serlcd(f'Pico on WLAN. \rIP: {ip}')

    
# HTTP server with socket
addr = ('0.0.0.0', 80)
s = socket()
# TODO better management of socket
s.close() #just in case it was bound
s = socket()
s.bind(addr)
s.listen(1)

msg_serlcd(f'Listening on\r{addr}', clear=False)

''' save this to pico as serlcd.html or load it directly:
with open('serlcd.html', 'r') as file:
    html = file.read()
'''

html = """<!DOCTYPE html>
<html>
    <head>
        <title>Pico W</title>
    </head>
    <body>
        <h1>Pico W</h1>
        <p>Say something to the SerLCD</p>
        <form>
            <input type="text" id="msg">
            <input type="button" onclick="window.open('?msg='+document.getElementById('msg').value+'&endof=msg','_self')" value="Say">
        </form>
    </body>
</html>
"""


# Listen for connections

def listen():
    try:
        c1, addr = s.accept()
        #msg_serlcd(f'Client connected from {addr}')
        print(f'client {addr}')
        r = c1.recv(1024)
        print(r)
        r = str(r)
        msgPos = r.find('?msg=')
        endPos = r.find('&endof=msg')
        hasMsg = msgPos > -1 and endPos > -1
        if hasMsg:
            print("some message there is")
            startPos = msgPos+5
            msg = r[startPos:endPos]
            # TODO need better unquote
            msg_unquoted = msg.replace('%20', ' ')
            print(f'Message: {msg_unquoted}')
            msg_serlcd(msg_unquoted)
        else:
            print("no message")
        c1.send('HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n')
        c1.send(html)
        c1.close()
    except OSError as e:
        c1.close()
        print('Connection closed')
        print(e)

try:
    while True:
        listen()
finally: # if stoped in Thonny. Unfortunately it does not work
    # clear serlcd otherwise it needs to be unplugged
    msg_serlcd("") # not working yet
    s.close() # unbind to be able to bind it next time
