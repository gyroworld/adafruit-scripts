#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import date, datetime


# Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'
options.show_refresh_rate = True
#options.limit_refresh_rate_hz = 120
options.disable_hardware_pulsing = False

# Create matrix and offscreen canvas
matrix = RGBMatrix(options=options)
offscreen_canvas = matrix.CreateFrameCanvas()

# Set fonts
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/6x10.bdf")

font_small = graphics.Font()
font_small.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/5x8.bdf")

font_smallest = graphics.Font()
font_smallest.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/4x6.bdf")

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

startTime = datetime.now()


def timeRunning():
    diff = datetime.now() - startTime
    hours = int(diff.seconds/3600)
    minutes = int((diff.seconds % 3600)/60)
    seconds = diff.seconds % 60
    return [hours, minutes, seconds]


def timerDisplay():
    global offscreen_canvas

    while True:
        offscreen_canvas.Clear()
        #time = timeRunning()

        graphics.DrawText(matrix, font_smallest, 8, 8, orange, "TIME")
        graphics.DrawText(matrix, font_smallest, 2, 17, purple, "RUNNING")
        #graphics.DrawText(matrix, font_small, -1, 28,light_blue, str('{:0>2}'.format(time[0])))
        #graphics.DrawText(matrix, font_small, 11, 28,light_blue, str('{:0>2}'.format(time[1])))
        #graphics.DrawText(matrix, font_small, 23, 28,light_blue, str('{:0>2}'.format(time[2])))
        graphics.DrawText(matrix, font_small, -1, 28,light_blue, str("01"))
        graphics.DrawText(matrix, font_small, 11, 28,light_blue, str("02"))
        graphics.DrawText(matrix, font_small, 23, 28,light_blue, str("03"))

        # Draw colon
        matrix.SetPixel(9, 24, 255, 255, 255)
        matrix.SetPixel(9, 25, 255, 255, 255)

        # Draw colon
        matrix.SetPixel(21, 24, 255, 255, 255)
        matrix.SetPixel(21, 25, 255, 255, 255)

        sleep(0.05)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)


timerDisplay()
