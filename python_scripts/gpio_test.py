import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
for x in range(0,10):
  GPIO.output(7,True)
  time.sleep(1)
  GPIO.output(7,False)
  time.sleep(1)
GPIO.cleanup()
