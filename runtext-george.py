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
    minutes = str(int(diff.seconds % 3600)/60)
    seconds = str(diff.seconds % 60)
    return [hours, minutes, seconds]

def test1():
    #DrawText(core.Canvas c, Font f, int x, int y, Color color, text):
    print("Running Test1.")
    graphics.DrawText(matrix, font, 9, 6, green, "NYE")
    graphics.DrawText(matrix, font, 6, 14, red, "2022")
    sleep(30)
    print("Test1 complete.")

def test2():
    print("Running test2.")
    i = 0
    global offscreen_canvas
    while i < 10:
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font, 0, 10, red, "Test2")
        sleep(0.5)
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        i += 1
    print("Test2 complete.")

def fontTest():
    print(font)
    print(font.CharacterWidth)
    print(font.height)
    print(font.baseline)

def happyNewYear():
    print("Running happyNewYear.")
    graphics.DrawText(matrix, font, 1, 8, green, "HAPPY")
    graphics.DrawText(matrix, font, 7, 16, red, "NEW")
    graphics.DrawText(matrix, font, 4, 24, purple, "YEAR")
    graphics.DrawText(matrix, font, 4, 32, blue, "2022")
    sleep(300)
    print("happyNewYear complete.")


happyNewYear()