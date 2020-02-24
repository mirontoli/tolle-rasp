// plot darkness. the darker surroundings, the lighter the leds. 
basic.forever(function () {
    led.plotBarGraph(
    1023 - pins.analogReadPin(AnalogPin.P0),
    1023
    )
})