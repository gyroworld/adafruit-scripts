#!/usr/bin/env python
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, GifImagePlugin

if len(sys.argv) < 2:
    sys.exit("Require an image argument")
else:
    image_file = sys.argv[1]

image = Image.open(image_file)

len = image.n_frames

#print(image.is_animated)

#print(image.n_frames)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.disable_hardware_pulsing = True

matrix = RGBMatrix(options = options)

# Make image fit our screen.
#image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'))

#image = image.resize((matrix.width, matrix.height))

while True:

    x = len

    for frame in range(0,x):

        image.seek(frame)
        image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
        matrix.SetImage(image.convert('RGB'))


    try:
        print("Press CTRL-C to stop.")
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        sys.exit(0)