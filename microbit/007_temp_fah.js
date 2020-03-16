let vol = 0
let tem = 0
let fah = 0
basic.forever(function () {
    vol = pins.map(
    pins.analogReadPin(AnalogPin.P0),
    0,
    1023,
    0,
    3170
    )
    tem = (vol - 500) / 10
    basic.showString("C")
    basic.showNumber(Math.round(tem))
    basic.pause(1000)
    fah = tem * (9 / 5) + 32
    basic.showString("F")
    basic.showNumber(Math.round(fah))
    basic.pause(1000)
})
