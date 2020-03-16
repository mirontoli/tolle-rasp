let vol = 0
let tem = 0
basic.forever(function () {
    vol = pins.map(
    pins.analogReadPin(AnalogPin.P0),
    0,
    1023,
    0,
    3170 //actual voltage when connected to the computer
    )
    tem = (vol - 500) / 10
    basic.showNumber(Math.round(tem))
    basic.pause(1000)
})
