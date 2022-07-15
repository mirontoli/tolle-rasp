# Use passive buzzer
# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import Speaker
speaker = Speaker(5)
speaker.play('c4', 1)