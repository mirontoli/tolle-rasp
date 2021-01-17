# a robot that opens his mouth to say hello when it hears a loud sound
def on_button_pressed_a():
    global cycles
    cycles = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cycles
    cycles = 6
input.on_button_pressed(Button.B, on_button_pressed_b)

cycles = 0
soundExpression.mysterious.play()
cycles = 0
basic.show_string("Stefan")

def on_forever():
    global cycles
    led.plot_bar_graph(input.sound_level(), 255)
    basic.pause(500)
    if input.sound_level() > 50:
        cycles = 0
    if cycles < 6:
        cycles += 1
        pins.servo_write_pin(AnalogPin.P1, 180)
        basic.show_number(cycles)
        basic.pause(500)
        pins.servo_write_pin(AnalogPin.P1, 60)
        soundExpression.hello.play()
        basic.show_number(cycles)
        basic.pause(500)
basic.forever(on_forever)
