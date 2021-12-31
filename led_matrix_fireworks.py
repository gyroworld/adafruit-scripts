#!/usr/bin/python

from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
from time import sleep
from datetime import datetime
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])


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
        offscreen_canvas.Clear()
        if i == 0:
            matrix.SetPixel(x, y, 255, 255, 255)

        elif i == 1:
            matrix.SetPixel(x, y, 255, 255, 255)

            matrix.SetPixel(x+1, y, 255, 255, 255)
            matrix.SetPixel(x-1, y, 255, 255, 255)
            matrix.SetPixel(x, y+1, 255, 255, 255)
            matrix.SetPixel(x, y-1, 255, 255, 255)

            matrix.SetPixel(x-1, y+1, 0, 255, 255)
            matrix.SetPixel(x+1, y+1, 0, 255, 255)
            matrix.SetPixel(x-1, y-1, 0, 255, 255)
            matrix.SetPixel(x+1, y-1, 0, 255, 255)

        elif i == 2:
            matrix.SetPixel(x, y, 0, 204, 204)

            matrix.SetPixel(x+1, y, 0, 255, 255)
            matrix.SetPixel(x-1, y, 0, 255, 255)
            matrix.SetPixel(x, y+1, 0, 255, 255)
            matrix.SetPixel(x, y-1, 0, 255, 255)
            matrix.SetPixel(x-1, y+1, 0, 255, 255)
            matrix.SetPixel(x-1, y-1, 0, 255, 255)
            matrix.SetPixel(x+1, y+1, 0, 255, 255)
            matrix.SetPixel(x+1, y-1, 0, 255, 255)

            matrix.SetPixel(x, y+2, 255, 255, 255)
            matrix.SetPixel(x+2, y+2, 255, 255, 255)
            matrix.SetPixel(x+2, y, 255, 255, 255)
            matrix.SetPixel(x+2, y-2, 255, 255, 255)
            matrix.SetPixel(x, y-2, 255, 255, 255)
            matrix.SetPixel(x-2, y-2, 255, 255, 255)
            matrix.SetPixel(x-2, y, 255, 255, 255)
            matrix.SetPixel(x-2, y+2, 255, 255, 255)

        
        elif i == 3:
            matrix.SetPixel(x, y, 0, 153, 153)

            matrix.SetPixel(x+1, y, 0, 204, 204)
            matrix.SetPixel(x-1, y, 0, 204, 204)
            matrix.SetPixel(x, y+1, 0, 204, 204)
            matrix.SetPixel(x, y-1, 0, 204, 204)
            matrix.SetPixel(x-1, y+1, 0, 204, 204)
            matrix.SetPixel(x-1, y-1, 0, 204, 204)
            matrix.SetPixel(x+1, y+1, 0, 204, 204)
            matrix.SetPixel(x+1, y-1, 0, 204, 204)

            matrix.SetPixel(x, y+2, 0, 255, 255)
            matrix.SetPixel(x+2, y+2, 0, 255, 255)
            matrix.SetPixel(x+2, y, 0, 255, 255)
            matrix.SetPixel(x+2, y-2, 0, 255, 255)
            matrix.SetPixel(x, y-2, 0, 255, 255)
            matrix.SetPixel(x-2, y-2, 0, 255, 255)
            matrix.SetPixel(x-2, y, 0, 255, 255)
            matrix.SetPixel(x-2, y+2, 0, 255, 255)
            
            matrix.SetPixel(x, y+3, 255, 255, 255)
            matrix.SetPixel(x+3, y+3, 255, 255, 255)
            matrix.SetPixel(x+3, y, 255, 255, 255)
            matrix.SetPixel(x+3, y-3, 255, 255, 255)
            matrix.SetPixel(x, y-3, 255, 255, 255)
            matrix.SetPixel(x-3, y-3, 255, 255, 255)
            matrix.SetPixel(x-3, y, 255, 255, 255)
            matrix.SetPixel(x-3, y+3, 255, 255, 255)

        elif i == 4:
            matrix.SetPixel(x, y, 0, 0, 0)

            matrix.SetPixel(x+1, y, 0, 153, 153)
            matrix.SetPixel(x-1, y, 0, 153, 153)
            matrix.SetPixel(x, y+1, 0, 153, 153)
            matrix.SetPixel(x, y-1, 0, 153, 153)
            matrix.SetPixel(x-1, y+1, 0, 153, 153)
            matrix.SetPixel(x-1, y-1, 0, 153, 153)
            matrix.SetPixel(x+1, y+1, 0, 153, 153)
            matrix.SetPixel(x+1, y-1, 0, 153, 153)

            matrix.SetPixel(x, y+2, 0, 204, 204)
            matrix.SetPixel(x+2, y+2, 0, 204, 204)
            matrix.SetPixel(x+2, y, 0, 204, 204)
            matrix.SetPixel(x+2, y-2, 0, 204, 204)
            matrix.SetPixel(x, y-2, 0, 204, 204)
            matrix.SetPixel(x-2, y-2, 0, 204, 204)
            matrix.SetPixel(x-2, y, 0, 204, 204)
            matrix.SetPixel(x-2, y+2, 0, 204, 204)
            
            matrix.SetPixel(x, y+3, 0, 255, 255)
            matrix.SetPixel(x+3, y+3, 0, 255, 255)
            matrix.SetPixel(x+3, y, 0, 255, 255)
            matrix.SetPixel(x+3, y-3, 0, 255, 255)
            matrix.SetPixel(x, y-3, 0, 255, 255)
            matrix.SetPixel(x-3, y-3, 0, 255, 255)
            matrix.SetPixel(x-3, y, 0, 255, 255)
            matrix.SetPixel(x-3, y+3, 0, 255, 255)
        
        elif i == 5:
            matrix.SetPixel(x, y, 0, 0, 0)

            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            matrix.SetPixel(x, y+2, 0, 153, 153)
            matrix.SetPixel(x+2, y+2, 0, 153, 153)
            matrix.SetPixel(x+2, y, 0, 153, 153)
            matrix.SetPixel(x+2, y-2, 0, 153, 153)
            matrix.SetPixel(x, y-2, 0, 153, 153)
            matrix.SetPixel(x-2, y-2, 0, 153, 153)
            matrix.SetPixel(x-2, y, 0, 153, 153)
            matrix.SetPixel(x-2, y+2, 0, 153, 153)
            
            matrix.SetPixel(x, y+3, 0, 204, 204)
            matrix.SetPixel(x+3, y+3, 0, 204, 204)
            matrix.SetPixel(x+3, y, 0, 204, 204)
            matrix.SetPixel(x+3, y-3, 0, 204, 204)
            matrix.SetPixel(x, y-3, 0, 204, 204)
            matrix.SetPixel(x-3, y-3, 0, 204, 204)
            matrix.SetPixel(x-3, y, 0, 204, 204)
            matrix.SetPixel(x-3, y+3, 0, 204, 204)

        elif i == 6:
            matrix.SetPixel(x, y, 0, 0, 0)

            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            matrix.SetPixel(x, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y, 0, 0, 0)
            matrix.SetPixel(x+2, y-2, 0, 0, 0)
            matrix.SetPixel(x, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y, 0, 0, 0)
            matrix.SetPixel(x-2, y+2, 0, 0, 0)
            
            matrix.SetPixel(x, y+3, 0, 153, 153)
            matrix.SetPixel(x+3, y+3, 0, 153, 153)
            matrix.SetPixel(x+3, y, 0, 153, 153)
            matrix.SetPixel(x+3, y-3, 0, 153, 153)
            matrix.SetPixel(x, y-3, 0, 153, 153)
            matrix.SetPixel(x-3, y-3, 0, 153, 153)
            matrix.SetPixel(x-3, y, 0, 153, 153)
            matrix.SetPixel(x-3, y+3, 0, 153, 153)

        elif i == 7:
            matrix.SetPixel(x, y, 0, 0, 0)

            matrix.SetPixel(x+1, y, 0, 0, 0)
            matrix.SetPixel(x-1, y, 0, 0, 0)
            matrix.SetPixel(x, y+1, 0, 0, 0)
            matrix.SetPixel(x, y-1, 0, 0, 0)
            matrix.SetPixel(x-1, y+1, 0, 0, 0)
            matrix.SetPixel(x-1, y-1, 0, 0, 0)
            matrix.SetPixel(x+1, y+1, 0, 0, 0)
            matrix.SetPixel(x+1, y-1, 0, 0, 0)

            matrix.SetPixel(x, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y+2, 0, 0, 0)
            matrix.SetPixel(x+2, y, 0, 0, 0)
            matrix.SetPixel(x+2, y-2, 0, 0, 0)
            matrix.SetPixel(x, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y-2, 0, 0, 0)
            matrix.SetPixel(x-2, y, 0, 0, 0)
            matrix.SetPixel(x-2, y+2, 0, 0, 0)
            
            matrix.SetPixel(x, y+3, 0, 0, 0)
            matrix.SetPixel(x+3, y+3, 0, 0, 0)
            matrix.SetPixel(x+3, y, 0, 0, 0)
            matrix.SetPixel(x+3, y-3, 0, 0, 0)
            matrix.SetPixel(x, y-3, 0, 0, 0)
            matrix.SetPixel(x-3, y-3, 0, 0, 0)
            matrix.SetPixel(x-3, y, 0, 0, 0)
            matrix.SetPixel(x-3, y+3, 0, 0, 0)

        offscreen_canvas = matrix.SwapOnVSync(offscreen_canvas)
        sleep(0.1)