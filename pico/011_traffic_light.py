# page 59 from "Get started with Raspberry Pi Pico"
import machine
import utime

led_red = machine.Pin(10, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(15, machine.Pin.OUT)

while True:
    # RED
    led_yellow.value(0)
    led_red.value(1)
    utime.sleep(5)
    # YELLOW
    led_red.value(0)
    led_yellow.value(1)
    utime.sleep(5)
    # GREEN
    led_yellow.value(0)
    led_green.value(1)
    utime.sleep(5)
    # YELLOW
    led_green.value(0)
    led_yellow.value(1)
    utime.sleep(5)
    # Start over - RED
    