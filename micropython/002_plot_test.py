# https://codewith.mu/en/tutorials/1.0/microbit
from microbit import *
flag = True

while True:
    sleep(100)
    if button_a.was_pressed():
        flag = not flag
    if flag:
        print((accelerometer.get_x(),))
    else:
        print(accelerometer.get_values())