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


#Create canvas
canvas = RGBMatrix(options = options)
offscreen_canvas = canvas.CreateFrameCanvas()

#Set font
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")

#Set color
textColor = graphics.Color(255, 0, 255)


#Draw line
#DrawLine(core.Canvas c, int x1, int y1, int x2, int y2, Color color)
#graphics.DrawLine(canvas, 1, 1, 10, 10, textColor)
#Drawing on screen
#time.sleep(5)

offscreen_canvas.Clear()
#DrawText(core.Canvas c, Font f, int x, int y, Color color, text):
graphics.DrawText(canvas, font, 1, 10, textColor, "Test")
canvas.SwapOnVSync(offscreen_canvas)

print('ran')
time.sleep(5)
print('complete')
