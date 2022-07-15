# This example gradually increases in frequency to create a positive sound:
# Use passive buzzer
# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import Speaker
from time import sleep
speaker = Speaker(5)

def win(): # rising frequency
    for i in range(2000, 5000, 100):
        speaker.play(i, 0.05)
win()        
