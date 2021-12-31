#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime


#Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True


#Create matrix and offscreen canvas
matrix = RGBMatrix(options = options)
offscreen_canvas = matrix.CreateFrameCanvas()

#Set font
font = graphics.Font()
#font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")

font_small = graphics.Font()
font_small.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")

#Set colors
purple = graphics.Color(255, 0, 255)
red = graphics.Color(255, 0, 0)
green = graphics.Color(0, 255, 0)
blue = graphics.Color(0, 0, 255)
white = graphics.Color(255, 255, 255)


def timeLeft():
    jan012022 = datetime(2022, 1, 1, 0, 0, 0, 0)
    now = datetime.now()
    diff = jan012022 - now
    hours = str(int(diff.seconds/3600))
    minutes = str(int((diff.seconds % 3600)/60))
    seconds = str(diff.seconds % 60)
    return [hours, minutes, seconds]

def test1():
    #DrawText(core.Canvas c, Font f, int x, int y, Color color, text):
    print("Running Test1.")
    graphics.DrawText(matrix, font, 9, 6, green, "NYE")
    graphics.DrawText(matrix, font, 6, 14, red, "2021")
    sleep(30)
    print("Test1 complete.")

def test2():
    global offscreen_canvas
    x = 32
    while True:
        time = timeLeft()
        offscreen_canvas.Clear()
        graphics.DrawText(matrix, font, 9, 8, green, "NYE")
        graphics.DrawText(matrix, font, 6, 16, red, "2021")
        graphics.DrawText(matrix, font, x, 24, purple, "Countdown")
        graphics.DrawText(matrix, font, 0, 32, blue, str(time[0]) + 'h' + str(time[1]) + 'm' + str(time[2]) + 's')
        
        x -= 1

        if (x == -53):
            x = 32

        sleep(0.1)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


def fontTest():
    print(font)
    print(font.CharacterWidth)
    print(font.height)
    print(font.baseline)

def happyNewYearStatic():
    print("Running happyNewYear.")
    graphics.DrawText(matrix, font, 1, 8, green, "HAPPY")
    graphics.DrawText(matrix, font, 7, 16, red, "NEW")
    graphics.DrawText(matrix, font, 4, 24, purple, "YEAR")
    graphics.DrawText(matrix, font, 4, 32, blue, "2022")
    sleep(300)
    print("happyNewYear complete.")


def happyNewYearScroll():
    global offscreen_canvas
    x1 = 32
    x2 = 44
    x3 = 56
    x4 = 68

    while True:
        offscreen_canvas.Clear()
        graphics.DrawText(matrix, font, x1, 8, green, "HAPPY")
        graphics.DrawText(matrix, font, x2, 16, red, "NEW")
        graphics.DrawText(matrix, font, x3, 24, purple, "YEAR")
        graphics.DrawText(matrix, font, x4, 32, blue, "2022")

        x1 -= 1
        x2 -= 1
        x3 -= 1
        x4 -= 1

        if (x1 == 0):
            x1 = 32
        if (x2 == 0):
            x2 = 44
        if (x3 == 0):
            x3 = 56
        if (x4 == 0):
            x4 = 68

        sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

def happyNewYearScroll2():
    global offscreen_canvas
    x = 32

    while True:
        offscreen_canvas.Clear()
        graphics.DrawText(matrix, font, x, 8, green, "HAPPY")
        graphics.DrawText(matrix, font, x+15, 16, red, "NEW")
        graphics.DrawText(matrix, font, x+24, 24, purple, "YEAR")
        graphics.DrawText(matrix, font, x+36, 32, blue, "2022")

        x -= 1

        if (x == -59):
            x = 32

        sleep(0.05)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)

test2()