#!/usr/bin/env python
import time
import sys
import os

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, GifImagePlugin

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True

matrix = RGBMatrix(options = options)

while True:
    for frame in range(0,14):
        image_file = f"'/home/pi/adafruit-scripts/frames{frame}.png'"
        image = Image.open(image_file)
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
        matrix.SetImage(image.convert('RGB'))
        time.sleep(0.1)
