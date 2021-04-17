# page 57 of "Get started with raspberry pi pico"
import machine
import utime

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

lit = False

while True:
    if button.value() == 1:
        if lit:
            led_external.value(0)
        else:
            led_external.value(1)
        lit = not lit
        utime.sleep(2)