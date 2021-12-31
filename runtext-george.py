#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime


# Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True

# Create matrix and offscreen canvas
matrix = RGBMatrix(options=options)
offscreen_canvas = matrix.CreateFrameCanvas()

# Set fonts
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")

font_small = graphics.Font()
font_small.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf")

font_large = graphics.Font()
font_large.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")

# Set colors
purple = graphics.Color(255, 0, 255)
red = graphics.Color(255, 0, 0)
green = graphics.Color(0, 255, 0)
blue = graphics.Color(0, 0, 255)
white = graphics.Color(255, 255, 255)
orange = graphics.Color(255, 128, 0)
light_blue = graphics.Color(0, 128, 255)
black = graphics.Color(0, 0, 0)


def timeLeft():
    jan012022 = datetime(2022, 1, 1, 0, 0, 0, 0)
    now = datetime.now()
    diff = jan012022 - now
    hours = str(int(diff.seconds/3600))
    minutes = str(int((diff.seconds % 3600)/60))
    seconds = str(diff.seconds % 60)
    return [hours, minutes, seconds]


def test1():
    # DrawText(core.Canvas c, Font f, int x, int y, Color color, text):
    print("Running Test1.")
    graphics.DrawText(matrix, font, 0, 6, green, "Looks")
    graphics.DrawText(matrix, font, 0, 14, red, "Good!")
    sleep(30)
    print("Test1 complete.")


def mainCountdownClock():
    global offscreen_canvas
    x = 32

    while True:
        offscreen_canvas.Clear()
        time = timeLeft()

        if time[0] == 0 and time[1] == 0:
            break

        graphics.DrawText(matrix, font, 8, 8, green, "NYE")
        graphics.DrawText(matrix, font, 5, 16, red, "2021")
        graphics.DrawText(matrix, font, x, 24, purple, "Countdown")
        graphics.DrawText(matrix, font_small, -1, 31, light_blue, str('{:0>2}'.format(time[0])))
        graphics.DrawText(matrix, font_small, 11, 31, light_blue, str('{:0>2}'.format(time[1])))
        graphics.DrawText(matrix, font_small, 22, 31, light_blue, str('{:0>2}'.format(time[2])))

        #matrix.SetPixel(10, 26, 255, 255, 255)
        matrix.SetPixel(9, 27, 255, 255, 255)
        matrix.SetPixel(9, 28, 255, 255, 255)
        #matrix.SetPixel(10, 30, 255, 255, 255)

        #matrix.SetPixel(21, 26, 255, 255, 255)
        matrix.SetPixel(21, 27, 255, 255, 255)
        matrix.SetPixel(21, 28, 255, 255, 255)
        #matrix.SetPixel(21, 30, 255, 255, 255)

        x -= 1

        if (x == -53):
            x = 32

        sleep(0.1)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


def fontTest(char):
    print('Character :' + str(char))
    print(font.CharacterWidth(char))
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


def happyNewYearFlashing():
    global offscreen_canvas
    offscreen_canvas.Clear()
    inverted = False
    i = 120

    while i > 0:
        if not inverted:
            graphics.DrawText(matrix, font, 1, 8, white, "HAPPY")
            graphics.DrawText(matrix, font, 7, 16, white, "NEW")
            graphics.DrawText(matrix, font, 4, 24, white, "YEAR")
            graphics.DrawText(matrix, font, 4, 32, white, "2022")
        else:
            matrix.Fill(255, 255, 255)
            graphics.DrawText(matrix, font, 1, 8, black, "HAPPY")
            graphics.DrawText(matrix, font, 7, 16, black, "NEW")
            graphics.DrawText(matrix, font, 4, 24, black, "YEAR")
            graphics.DrawText(matrix, font, 4, 32, black, "2022")
        sleep(0.5)
        i -= 1
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


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


def minuteCountdown():
    global offscreen_canvas

    while True:
        offscreen_canvas.Clear()
        time = timeLeft()

        if time[2] == 0:
            break

        graphics.DrawText(offscreen_canvas, font, 1, 26, white, str('{:0>2}'.format(time[2])))
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        sleep(.1)


def main():
    mainCountdownClock()
    minuteCountdown()
    happyNewYearFlashing()
    happyNewYearScroll2()
