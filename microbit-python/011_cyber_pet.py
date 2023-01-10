from microbit import *
while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    elif button_b.is_pressed():
        break
    # checking for both buttons did not work for me
    elif button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SURPRISED)
    else:
        display.show(Image.SAD)

display.clear()