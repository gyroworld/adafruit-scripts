#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

c1r = int(sys.argv[3])
c1g = int(sys.argv[4])
c1b = int(sys.argv[5])

c2r = int(sys.argv[6])
c2g = int(sys.argv[7])
c2b = int(sys.argv[8])

c3r = int(sys.argv[9])
c3g = int(sys.argv[10])
c3b = int(sys.argv[11])

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

#blue green firework
while True:
    for i in range(8):
        #offscreen_canvas.Clear()
        if i == 0:
            #Center pixel
            matrix.SetPixel(x, y, 255, 255, 255)

        elif i == 1:
            #Center pixel
            matrix.SetPixel(x, y, c1r, c1g, c1b)

            #Center cross
            matrix.SetPixel(x+1, y, 255, 255, 255)
            matrix.SetPixel(x-1, y, 255, 255, 255)
            matrix.SetPixel(x, y+1, 255, 255, 255)
            matrix.SetPixel(x, y-1, 255, 255, 255)

            #Center square
            #matrix.SetPixel(x-1, y+1, c1r, c1g, c1b)
            #matrix.SetPixel(x+1, y+1, c1r, c1g, c1b)
            #matrix.SetPixel(x-1, y-1, c1r, c1g, c1b)
            #matrix.SetPixel(x+1, y-1, c1r, c1g, c1b)

        elif i == 2:
            #Center pixel
            matrix.SetPixel(x, y, c2r, c2g, c2b)

            #Center cross
            matrix.SetPixel(x+1, y, c2r, c2g, c2b)
            matrix.SetPixel(x-1, y, c2r, c2g, c2b)
            matrix.SetPixel(x, y+1, c2r, c2g, c2b)
            matrix.SetPixel(x, y-1, c2r, c2g, c2b)

            #Center square
            matrix.SetPixel(x-1, y+1, c1r, c1g, c1b)
            matrix.SetPixel(x-1, y-1, c1r, c1g, c1b)
            matrix.SetPixel(x+1, y+1, c1r, c1g, c1b)
            matrix.SetPixel(x+1, y-1, c1r, c1g, c1b)

            #Middle square
            matrix.SetPixel(x, y+2, 255, 255, 255)
            #matrix.SetPixel(x+2, y+2, 255, 255, 255)
            matrix.SetPixel(x+2, y, 255, 255, 255)
            #matrix.SetPixel(x+2, y-2, 255, 255, 255)
            matrix.SetPixel(x, y-2, 255, 255, 255)
            #matrix.SetPixel(x-2, y-2, 255, 255, 255)
            matrix.SetPixel(x-2, y, 255, 255, 255)
            #matrix.SetPixel(x-2, y+2, 255, 255, 255)

        
        elif i == 3:
            #Center pixel
            matrix.SetPixel(x, y, c3r, c3g, c3b)

            #Center cross
            matrix.SetPixel(x+1, y, c3r, c3g, c3b)
            matrix.SetPixel(x-1, y, c3r, c3g, c3b)
            matrix.SetPixel(x, y+1, c3r, c3g, c3b)
            matrix.SetPixel(x, y-1, c3r, c3g, c3b)
            
            #Center square
            matrix.SetPixel(x-1, y+1, c2r, c2g, c2b)
            matrix.SetPixel(x-1, y-1, c2r, c2g, c2b)
            matrix.SetPixel(x+1, y+1, c2r, c2g, c2b)
            matrix.SetPixel(x+1, y-1, c2r, c2g, c2b)

            #Middle square
            matrix.SetPixel(x, y+2, c1r, c1g, c1b)
            matrix.SetPixel(x+2, y+2, 255, 255, 255)
            matrix.SetPixel(x+2, y, c1r, c1g, c1b)
            matrix.SetPixel(x+2, y-2, 255, 255, 255)
            matrix.SetPixel(x, y-2, c1r, c1g, c1b)
            matrix.SetPixel(x-2, y-2, 255, 255, 255)
            matrix.SetPixel(x-2, y, c1r, c1g, c1b)
            matrix.SetPixel(x-2, y+2, 255, 255, 255)
            
            #Outer square
            matrix.SetPixel(x, y+3, 255, 255, 255)
            #matrix.SetPixel(x+3, y+3, 255, 255, 255)
            matrix.SetPixel(x+3, y, 255, 255, 255)
            #matrix.SetPixel(x+3, y-3, 255, 255, 255)
            matrix.SetPixel(x, y-3, 255, 255, 255)
            #matrix.SetPixel(x-3, y-3, 255, 255, 255)
            matrix.SetPixel(x-3, y, 255, 255, 255)
            #matrix.SetPixel(x-3, y+3, 255, 255, 255)

        elif i == 4:
            #Center pixel
            matrix.SetPixel(x, y, 0, 0, 0)

            #Center cross
            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)

            #Center square
            matrix.SetPixel(x-1, y+1, 0, 54, 54)
            matrix.SetPixel(x-1, y-1, 0, 54, 54)
            matrix.SetPixel(x+1, y+1, 0, 54, 54)
            matrix.SetPixel(x+1, y-1, 0, 54, 54)

            #Middle square
            matrix.SetPixel(x, y+2, c2r, c2g, c2b)
            matrix.SetPixel(x+2, y+2, c2r, c2g, c2b)
            matrix.SetPixel(x+2, y, c2r, c2g, c2b)
            matrix.SetPixel(x+2, y-2, c2r, c2g, c2b)
            matrix.SetPixel(x, y-2, c2r, c2g, c2b)
            matrix.SetPixel(x-2, y-2, c2r, c2g, c2b)
            matrix.SetPixel(x-2, y, c2r, c2g, c2b)
            matrix.SetPixel(x-2, y+2, c2r, c2g, c2b)
            
            #Outer square
            matrix.SetPixel(x, y+3, c1r, c1g, c1b)
            #matrix.SetPixel(x+3, y+3, c1r, c1g, c1b)
            matrix.SetPixel(x+3, y, c1r, c1g, c1b)
            #matrix.SetPixel(x+3, y-3, c1r, c1g, c1b)
            matrix.SetPixel(x, y-3, c1r, c1g, c1b)
            #matrix.SetPixel(x-3, y-3, c1r, c1g, c1b)
            matrix.SetPixel(x-3, y, c1r, c1g, c1b)
            #matrix.SetPixel(x-3, y+3, c1r, c1g, c1b)
        
        elif i == 5:
            #Center pixel
            matrix.SetPixel(x, y, 0, 0, 0)

            #Center cross
            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)

            #Center square
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            #Middle square
            matrix.SetPixel(x, y+2, 0, 54, 54)
            matrix.SetPixel(x+2, y+2, 0, 54, 54)
            matrix.SetPixel(x+2, y, 0, 54, 54)
            matrix.SetPixel(x+2, y-2, 0, 54, 54)
            matrix.SetPixel(x, y-2, 0, 54, 54)
            matrix.SetPixel(x-2, y-2, 0, 54, 54)
            matrix.SetPixel(x-2, y, 0, 54, 54)
            matrix.SetPixel(x-2, y+2, 0, 54, 54)
            
            matrix.SetPixel(x, y+3, c2r, c2g, c2b)
            #matrix.SetPixel(x+3, y+3, c2r, c2g, c2b)
            matrix.SetPixel(x+3, y, c2r, c2g, c2b)
            #matrix.SetPixel(x+3, y-3, c2r, c2g, c2b)
            matrix.SetPixel(x, y-3, c2r, c2g, c2b)
            #matrix.SetPixel(x-3, y-3, c2r, c2g, c2b)
            matrix.SetPixel(x-3, y, c2r, c2g, c2b)
            #matrix.SetPixel(x-3, y+3, c2r, c2g, c2b)

        elif i == 6:
            #Center pixel
            matrix.SetPixel(x, y, 0, 0, 0)

            #Center cross
            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)

            #Center square
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            #Middle square
            matrix.SetPixel(x, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y, 0, 0, 0)
            matrix.SetPixel(x+2, y-2, 0, 0, 0)
            matrix.SetPixel(x, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y, 0, 0, 0)
            matrix.SetPixel(x-2, y+2, 0, 0, 0)
            
            #Outer square
            matrix.SetPixel(x, y+3, 0, 54, 54)
            #matrix.SetPixel(x+3, y+3, 0, 54, 54)
            matrix.SetPixel(x+3, y, 0, 54, 54)
            #matrix.SetPixel(x+3, y-3, 0, 54, 54)
            matrix.SetPixel(x, y-3, 0, 54, 54)
            #matrix.SetPixel(x-3, y-3, 0, 54, 54)
            matrix.SetPixel(x-3, y, 0, 54, 54)
            #matrix.SetPixel(x-3, y+3, 0, 54, 54)

        elif i == 7:
            #Center pixel
            matrix.SetPixel(x, y, 0, 0, 0)

            #Center cross
            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)

            #Center square
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            #Middle square
            matrix.SetPixel(x, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y, 0, 0, 0)
            matrix.SetPixel(x+2, y-2, 0, 0, 0)
            matrix.SetPixel(x, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y, 0, 0, 0)
            matrix.SetPixel(x-2, y+2, 0, 0, 0)
            
            #Outer square
            matrix.SetPixel(x, y+3, 0, 0, 0)
            matrix.SetPixel(x+3, y+3, 0, 0, 0)
            matrix.SetPixel(x+3, y, 0, 0, 0)
            matrix.SetPixel(x+3, y-3, 0, 0, 0)
            matrix.SetPixel(x, y-3, 0, 0, 0)
            matrix.SetPixel(x-3, y-3, 0, 0, 0)
            matrix.SetPixel(x-3, y, 0, 0, 0)
            matrix.SetPixel(x-3, y+3, 0, 0, 0)

        #offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        sleep(.05)

    else:
        #offscreen_canvas.Clear()
        #offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        sleep(2)