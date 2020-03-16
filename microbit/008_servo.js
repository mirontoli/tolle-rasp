basic.forever(function () {
    pins.servoWritePin(AnalogPin.P1, 0)
    basic.pause(2000)
    pins.servoWritePin(AnalogPin.P1, 180)
    basic.pause(2000)
})