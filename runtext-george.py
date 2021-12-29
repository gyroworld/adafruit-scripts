#!/usr/bin/python
#import sys
#sys.path.append('/home/pi/rpi-rgb-led-matrix/bindings/python/samples')
#from samplebase import SampleBase
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time

#Set matrix options
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.disable_hardware_pulsing = True
matrix = RGBMatrix(options = options)

#Set font
font_file = "/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf"
font = graphics.Font().LoadFont(font_file)

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


"""
class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")
        textColor = graphics.Color(255, 0, 255)
        pos = offscreen_canvas.width
        my_text = self.args.text

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
"""