let PhoVal = 0
let CalVal = pins.analogReadPin(AnalogPin.P0)
basic.forever(function () {
    PhoVal = pins.analogReadPin(AnalogPin.P0)
    if (PhoVal < CalVal - 2) {
        basic.showIcon(IconNames.Angry)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
