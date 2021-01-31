# https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html#ticklish-python
from microbit import *
while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)