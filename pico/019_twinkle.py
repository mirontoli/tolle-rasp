# Twinkle twinkle little star
# Use passive buzzer
# https://projects.raspberrypi.org/en/projects/sensory-gadget/2
from picozero import Speaker
speaker = Speaker(5)
b = 1 # beat
C = ['c4', b]
Cx2 = ['c4', b*2]
D = ['d4', b]
Dx2 = ['d4', b*2]
E = ['e4', b]
Ex2 = ['e4', b*2]
F = ['f4', b]
Fx2 = ['f4', b*2]
G = ['g4', b]
Gx2 = ['g4', b*2]
A = ['a4', b]

start = [ C, C, G, G, A, A, Gx2, F, F, E, E, D, D, Cx2 ]
middle = [ G, G, F, F, E, E, Dx2 ]
speaker.play(start)
speaker.play(middle)
speaker.play(middle)
speaker.play(start)