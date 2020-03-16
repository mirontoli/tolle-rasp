control.onEvent(EventBusSource.MICROBIT_ID_IO_P0, EventBusValue.MICROBIT_PIN_EVT_FALL, function () {
    pins.digitalWritePin(DigitalPin.P2, 1)
    basic.showIcon(IconNames.SmallSquare)
})
control.onEvent(EventBusSource.MICROBIT_ID_IO_P0, EventBusValue.MICROBIT_PIN_EVT_RISE, function () {
    pins.digitalWritePin(DigitalPin.P2, 0)
    basic.showIcon(IconNames.Square)
})
pins.setEvents(DigitalPin.P0, PinEventType.Edge)
pins.setPull(DigitalPin.P0, PinPullMode.PullUp)