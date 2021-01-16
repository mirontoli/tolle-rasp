# sample script from
# https://pinout.xyz/pinout/unicorn_phat
# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-unicorn-phat
# to run type: sudo python3 unicorn01.py
import unicornhat as uh
import time
uh.set_layout(uh.PHAT)
uh.brightness(0.5)
uh.set_pixel(0, 0, 255, 0, 0)
uh.show()
# we need to pause, once it exits, the led goes out
time.sleep(2)
uh.clear()
uh.show()
time.sleep(1)

for x in range(8):
  for y in range(4):
    uh.set_pixel(x,y,0,255,255)
uh.show()
time.sleep(10)

