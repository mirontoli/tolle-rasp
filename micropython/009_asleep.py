#https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html#event-loops
from microbit import *
while running_time() < 10000:
    display.show(Image.ASLEEP)
    
display.show(Image.SURPRISED)