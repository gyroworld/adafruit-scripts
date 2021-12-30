#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics, FrameCanvas
import time

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
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

#Set color
purple = graphics.Color(255, 0, 255)
red = graphics.Color(255, 0, 0)



#Draw line
#DrawLine(core.Canvas c, int x1, int y1, int x2, int y2, Color color)
#graphics.DrawLine(matrix, 1, 1, 10, 10, textColor)
#Drawing on screen
#time.sleep(5)

#DrawText(core.Canvas c, Font f, int x, int y, Color color, text):
print("Running test1.")
graphics.DrawText(matrix, font, 1, 10, purple, "Test1")
time.sleep(5)
print("Test1 complete.")

print("Running test2.")
i = 0
while i < 10:
    offscreen_canvas.Clear()
    graphics.DrawText(offscreen_canvas, font, 1, 10, red, "Test2")
    time.sleep(0.5)
    offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
    i += 1
print("Test2 complete.")
