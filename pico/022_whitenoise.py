# This example gradually increases in frequency to create a positive sound:
# Use passive buzzer
# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import Speaker
from time import sleep
from random import randint
speaker = Speaker(5)

for i in range(100):
    speaker.play(randint(500, 5000))
    sleep(0.001)
    speaker.off() # stop in the example did not work: Speaker has no attribute stop
    sleep(0.05)