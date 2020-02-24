basic.forever(function () {
    led.plotBarGraph(
        pins.analogReadPin(AnalogPin.P0),
        1023
    )
})
