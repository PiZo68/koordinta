def on_forever():
    led.plot_brightness(randint(0, 4), randint(0, 4), randint(0, 255))
    basic.pause(500)
    basic.clear_screen()
basic.forever(on_forever)
