let item = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
item.showRainbow(1, 360)
basic.forever(function () {
    item.show()
    item.rotate(1)
    basic.pause(100)
})