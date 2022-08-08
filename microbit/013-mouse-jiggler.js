basic.forever(function () {
    pins.servoWritePin(AnalogPin.P2, randint(1, 180))
    basic.pause(30000)
})
