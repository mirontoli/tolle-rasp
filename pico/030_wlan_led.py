'''
just connect to wlan and light the onboard led
2023-01-07
https://bitluni.net/screen-sharing-matrix
https://gitlab.com/florindragan/raspberry_pico_w_websocket/-/blob/main/percentage.html
https://microcontrollerslab.com/raspberry-pi-pico-w-web-server-control-led/
https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications
https://how2electronics.com/raspberry-pi-pico-w-web-server-tutorial-with-micropython/
https://www.petecodes.co.uk/creating-a-basic-raspberry-pi-pico-web-server-using-micropython/
https://www.youtube.com/watch?v=yzRHAdS9FLY&ab_channel=bitluni
https://stackoverflow.com/questions/74551529/raspi-pico-w-errno-98-eaddrinuse-despite-using-socket-so-reuseaddr
https://forum.micropython.org/viewtopic.php?t=2793
'''

from machine import Pin
from time import sleep
from secrets import secrets
import network
from socket import socket, getaddrinfo
# import gc

led = Pin('LED', Pin.OUT)
led.value(0)

# gc.collect()
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
    led.value(1)

# http server
addr = ('', 80)
s = socket()
s.bind(addr)
s.listen(1)

# save the html file on pico
with open('030_wlan_led.html', 'r') as file:
    html = file.read()


def listen():
    try:
        c1, addr = s.accept()
        print(f'client {addr}')
        r = c1.recv(1024)
        if r[0] == 80:  # P for POST
            print(r)
            '''
            for i in range(len(r) - 3 ):
                if r[i] == 13 and r[i+1] == 10 and r[i+2] == 13 and r[i+3] == 10:
                    #found post body start
                    start = i+4
            
            payload = r[start:-1]
            '''
            print('received a POST')
            # payload = r.decode('utf-8').split('\r\n\r\n')[1]
            # print(f'payload: {payload}')
            last_char = r[-1]
            print(f'last char: {last_char}')
            if last_char == 70:  # F
                direction = "forward"
            elif last_char == 66:  # B
                direction = "backward"
            elif last_char == 76:  # L
                direction == "left"
            elif last_char == 82:  # R
                direction = "right"
            print(f'going to the {direction}')
            c1.send('HTTP/1.0 202 Accepted\r\n')
        if r[0] == 71:  # G for GET
            c1.send('HTTP/1.0 200 OK\r\nContent-Type:text/html\r\n\r\n')
            c1.send(html)
        c1.close()
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
