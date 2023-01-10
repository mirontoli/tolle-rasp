from microbit import *
pattern = '0{n}{n}{n}0:{n}{n}{n}{n}{n}:{n}{n}{n}{n}{n}:{n}{n}{n}{n}{n}:0{n}{n}{n}0'
#image1 = Image(pattern.format(n=9))
fadein = list(map(lambda x: Image(pattern.format(n=x)), range(10)))
fadeout = reversed(fadein)

while True:
    display.show(fadein, delay=300)
    sleep(1000)
    display.show(fadeout, delay=300)
    sleep(1000)
