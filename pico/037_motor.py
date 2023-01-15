'''
https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/
https://microdigisoft.com/control-dc-motor-using-l298n-raspberry-pi-pico-micropython/
https://www.youtube.com/watch?v=H1Fzil_VUq4&ab_channel=NerdCave
curl.exe https://gabmus.org/pico_pinout

common ground
GP4 - 06 - ENA (blue)
GP3 - 05 - IN1 (red)
GP2 - 04 - IN2 (green)
GND - 18 - Common ground

CASE 1:
4x1.2v rechargeable batteries = 5.37v
l298n 5v output = 3.96v
OUT1 0.124 v only, produces only noise, no motion

CASE 2:
9.04 v
l298n 5v output = 4.95v
OUT1 0.245 v only, produces only noise, no motion

CASE 3:
if 5v jumper removed, the motor does not start

CASE 4:
if ENA jumper is connected, 9v battery = 9.03v
motor out1 1.63v, motor not starting

CASE 5:
ENA is connected, 9v battery = 9.02v
Motor1 is disconnected
OUT1 = 8.45v

CASE 6: 
ENA is connected, 9v battery
Motor1 is a smaller motor, and it works. 

CASE 7:
ENA is connected, barrel jack connected to 5v 2A.
pico is disconnected
5v output is connected to in1
Motor runs, 2.42v is coming out to out1

CASE 8
ENA is connected, 4 alkaline AA batteries 5.11v
5v out connected to in1, no noise, no motion

CASE 9:
ENA is connected, 12v 1A charger plugged in
12.01 v in
when connected in1, 8.78v goes to motor
motor works fine

CASE 10:
ENA is connected, a 23A battery 12v is connected
input 12.31v
when connected in1, motor sounds for a second, 
then it is quite, no motion at all, approx 0.250 A
in1 disconnected => 0.025 A

CASE 11:
powerbank connected 5.16v
when connected to in1, 0.896v, 0.307A
when not connected, 0.022A

CASE 12:
charger 5v 2A, 5.17v 
in1 disconnected 0.022A
in1 connected 4.28v 0.498A to motor 1.62v, when measured, motor cannot run
when not measured, motor runs but slowly

'''

from machine import Pin, PWM
from time import sleep

in1 = Pin(3, Pin.OUT)
in2 = Pin(2, Pin.OUT)

speed = PWM(Pin(4))
speed.freq(1000)
speed.duty_u16(10000)
in1.low()  # spin forward
in2.high()
