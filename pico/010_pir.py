# page 82 from "Get started with Raspberry Pi Pico"
import machine
import utime

sensor_pir = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(14, machine.Pin.OUT)

def pir_handler(pin):
    utime.sleep_ms(100)
    if pin.value():
        print('ALARM! Motion detected!')
        buzzer.value(1)
        utime.sleep(2)
        buzzer.value(0)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)