'''
https://github.com/BetaRavener/upy-websocket-server/blob/master/ws_connection.py
https://github.com/marcidy/micropython-uasyncio-webexample/blob/main/examples/websocket/runme.py
'''
import sys
import binascii
import hashlib

import machine
import network
import socket
from time import sleep
from secrets import secrets

from websocket import websocket

led = machine.Pin('LED', machine.Pin.OUT)
led.value(0)


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
    led.value(1)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ai = socket.getaddrinfo('0.0.0.0', 80)
addr = ai[0][4]
s.bind(addr)
s.listen(1)

# save the html file on pico
with open('030_wlan_led.html', 'r') as file:
    html = file.read()

DEBUG = 1


def server_handshake(sock):
    clr = sock.makefile("rwb", 0)
    l = clr.readline()
    # sys.stdout.write(repr(l))

    webkey = None

    while 1:
        l = clr.readline()
        if not l:
            raise OSError("EOF in headers")
        if l == b"\r\n":
            break
    #    sys.stdout.write(l)
        h, v = [x.strip() for x in l.split(b":", 1)]
        if DEBUG:
            print((h, v))
        if h == b'Sec-WebSocket-Key':
            webkey = v

    if not webkey:
        raise OSError("Not a websocket request")

    if DEBUG:
        print("Sec-WebSocket-Key:", webkey, len(webkey))

    d = hashlib.sha1(webkey)
    d.update(b"258EAFA5-E914-47DA-95CA-C5AB0DC85B11")
    respkey = d.digest()
    respkey = binascii.b2a_base64(respkey)[:-1]
    if DEBUG:
        print("respkey:", respkey)

    sock.send(b"""\
HTTP/1.1 101 Switching Protocols\r
Upgrade: websocket\r
Connection: Upgrade\r
Sec-WebSocket-Accept: """)
    sock.send(respkey)
    sock.send("\r\n\r\n")


def read():
    msg_bytes = None
    try:
        msg_bytes = ws.read()
    except OSError:
        pass

    return msg_bytes


def _accept_conn(listen_sock):
    cl, remote_addr = listen_sock.accept()
    print("Client connection from:", remote_addr)

    try:
        server_handshake(cl)
    except OSError:
        # Not a websocket connection, serve webpage
        pass


def _setup_conn(port=81, accept_handler=_accept_conn):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ai = socket.getaddrinfo("0.0.0.0", port)
    addr = ai[0][4]

    s.bind(addr)
    s.listen(1)
    if accept_handler:
        s.setsockopt(socket.SOL_SOCKET, 20, accept_handler)
    for i in (network.AP_IF, network.STA_IF):
        iface = network.WLAN(i)
        if iface.active():
            print("WebSocket started on ws://%s:%d" %
                  (iface.ifconfig()[0], port))
    ws = websocket(s, True)


def listen():
    try:
        c1, addr = s.accept()
        print(f'client {addr}')
        _setup_conn()
        # server_handshake(c1)
        # ws = websocket(s, True)
        # msg_bytes = ws.read()
        # print(f'msg_bytes {msg_bytes}')
    except OSError as e:
        c1.close()
        print('Connection closed')
        print(e)


try:
    while True:
        listen()
except KeyboardInterrupt:
    machine.reset()
finally:
    print("finally block")
    s.close()
