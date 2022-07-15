# Use passive buzzer
# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import Speaker
from time import sleep
speaker = Speaker(5)

def chirp(): # series of high-pitched chirps
    for _ in range(2):
        for i in range(5000, 2999, -100):
            speaker.play(i, 0.02) # very short duration
        sleep(0.02)
        
chirp()