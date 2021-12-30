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
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/10x20.bdf")
#font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/texgyre-27.bdf")

#Set colors
purple = graphics.Color(255, 0, 255)
red = graphics.Color(255, 0, 0)
green = graphics.Color(0, 255, 0)
blue = graphics.Color(0, 0, 255)
white = graphics.Color(255, 255, 255)

def countdown():
    print("Running countdown timer.")
    i = 59
    global offscreen_canvas
    while i > 0:
        offscreen_canvas.Clear()
        graphics.DrawText(offscreen_canvas, font, 0, 10, white, str(i))
        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        sleep(1)
        i -= 1
    print("Countdown timer complete.")

countdown()
