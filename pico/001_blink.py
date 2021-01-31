from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer = Timer()
led.toggle()

def blink(timer):
    led.toggle()
    
timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)