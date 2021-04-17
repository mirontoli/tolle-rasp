# page 53 of "Get started with raspberry pi pico"
# a six-legged button from microbit kit does not work
# a four-legged button works
import machine
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("You pressed the button!")
        utime.sleep(2)
