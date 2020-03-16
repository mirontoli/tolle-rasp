//this script shows the brightness with servo
let phoVal = 0 //photocell value, from 0 to 1023
let serVal = 0 // servo value, from 0 to 180
basic.forever(function () {
    phoVal = pins.analogReadPin(AnalogPin.P0)
    serVal = pins.map(phoVal, 0, 1023, 0, 180)
    pins.servoWritePin(AnalogPin.P1, serVal)
})