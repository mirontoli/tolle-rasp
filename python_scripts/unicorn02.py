import unicornhat as uh
import time

uh.set_layout(uh.PHAT)
uh.brightness(0.5)

def paint(r, g, b):
  for x in range(8):
    for y in range(4):
      uh.set_pixel(x,y,r,g, b)
  uh.show()

while True:
  paint(0,255,0)
  time.sleep(10)
  paint(255,255,0)
  time.sleep(10)
  paint(255,0,0)
  time.sleep(10)





