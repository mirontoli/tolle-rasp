# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import LED
from time import sleep
led = LED(13)
led.on()
sleep(1)
led.off()
