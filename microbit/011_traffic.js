//red - yellow - green 
let item = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
basic.forever(function () {
    item.showColor(neopixel.colors(NeoPixelColors.Red))
    basic.pause(2000)
    basic.pause(2000)
    item.showColor(neopixel.colors(NeoPixelColors.Yellow))
    basic.pause(2000)
    item.showColor(neopixel.colors(NeoPixelColors.Green))
    basic.pause(2000)
    basic.pause(2000)
})