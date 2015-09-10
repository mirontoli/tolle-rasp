#2015-09-10
#pin 7 (+) goes to a led light then resistor
#then to the pin 6 (gnd)
#inspired by Explaining Computers: 
#Raspberry Pi Robotics #1: GPIO Control
#https://www.youtube.com/watch?v=41IO4Qe5Jzw
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
