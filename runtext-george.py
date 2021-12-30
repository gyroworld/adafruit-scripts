#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

#Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.cols = 32
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

#Create canvas
offscreen_canvas = matrix.CreateFrameCanvas()

#Set font
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

#Set color
textColor = graphics.Color(255, 0, 255)


#Draw line
#DrawLine(core.Canvas c, int x1, int y1, int x2, int y2, Color color)
graphics.DrawLine(matrix, 1, 1, 10, 10, textColor)
#Drawing on screen
time.sleep(5)

offscreen_canvas.Clear()
graphics.DrawText(offscreen_canvas, font, 32, 10, textColor, "Test")
matrix.SwapOnVSync(offscreen_canvas)

print('ran')
time.sleep(5)
print('complete')
