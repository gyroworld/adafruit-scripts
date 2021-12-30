#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

#Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

#Set font
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

#Set color
textColor = graphics.Color(255, 0, 255)

#Drawing on screen
offscreen_canvas = matrix.CreateFrameCanvas()
#offscreen_canvas.Clear()
graphics.DrawText(offscreen_canvas, font, 32, 10, textColor, "Test")
#matrix.SwapOnVSync(offscreen_canvas)

print('ran')
time.sleep(5)
print('complete')
