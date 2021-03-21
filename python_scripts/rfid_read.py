"""
This is the code from a tutorial: https://pimylifeup.com/raspberry-pi-rfid-rc522/
you need to enable SPI on you Raspberry Pi
you need to install spidev and mfrc522 with pip3
Tried on my RPi3
"""
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    id, text = reader.read()
    print(id)
    print(text)
finally:
    GPIO.cleanup()

