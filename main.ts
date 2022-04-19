basic.forever(function () {
    led.plotBrightness(randint(0, 4), randint(0, 4), randint(0, 255))
    basic.pause(500)
    basic.clearScreen()
})
