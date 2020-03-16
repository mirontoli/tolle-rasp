function showOnePixel (start: number) {
    item.clear()
    range = item.range(start, 1)
    range.showColor(neopixel.colors(NeoPixelColors.Green))
    basic.pause(1000)
}
let range: neopixel.Strip = null
let item: neopixel.Strip = null
item = neopixel.create(DigitalPin.P0, 8, NeoPixelMode.RGB)
basic.forever(function () {
    for (let index = 0; index <= 7; index++) {
        showOnePixel(index)
    }
})
