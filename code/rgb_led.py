# NeoPixels must be connected to D10, D12, D18 or D21
# sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
# sudo python3 - m pip install - -force-reinstall adafruit-blinka

import time
import board
import neopixel


class Neopixels:
    def __init__(self):
        self.pixel_pin = board.D18
        self.num_pixels = 64
        self.ORDER = neopixel.GRB

        self.pixels = neopixel.NeoPixel(
            self.pixel_pin, self.num_pixels, brightness=0.2, auto_write=False, pixel_order=self.ORDER
        )

    def wheel(self, pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b) if self.ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.num_pixels):
                pixel_index = (i * 256 // self.num_pixels) + j
                self.pixels[i] = self.wheel(pixel_index & 255)
            self.pixels.show()
            time.sleep(wait)

    # Run tests or entertain the user
    def test(self):
        self.pixels.fill((255, 0, 0))
        self.pixels.show()
        time.sleep(1)

        self.pixels.fill((0, 255, 0))
        self.pixels.show()
        time.sleep(1)

        self.pixels.fill((0, 0, 255))
        self.pixels.show()
        time.sleep(1)

        self.rainbow_cycle(0.001)  # rainbow cycle with 1ms delay per step

    # Set pixel at given position with specified colour
    def set_pixel_at_position(self, position, colour):
        position_map = {
            "a8": 0, "b8": 1, "c8": 2, "d8": 3, "e8": 4, "f8": 5, "g8": 6, "h8": 7,
            "a7": 8, "b7": 9, "c7": 10, "d7": 11, "e7": 12, "f7": 13, "g7": 14, "h7": 15,
            "a6": 16, "b6": 17, "c6": 18, "d6": 19, "e6": 20, "f6": 21, "g6": 22, "h6": 23,
            "a5": 24, "b5": 25, "c5": 26, "d5": 27, "e5": 28, "f5": 29, "g5": 30, "h5": 31,
            "a4": 32, "b4": 33, "c4": 34, "d4": 35, "e4": 36, "f4": 37, "g4": 38, "h4": 39,
            "a3": 40, "b3": 41, "c3": 42, "d3": 43, "e3": 44, "f3": 45, "g3": 46, "h3": 47,
            "a2": 48, "b2": 49, "c2": 50, "d2": 51, "e2": 52, "f2": 53, "g2": 54, "h2": 55,
            "a1": 56, "b1": 57, "c1": 58, "d1": 59, "e1": 60, "f1": 61, "g1": 62, "h1": 63
        }

        self.pixels[position_map[position]] = colour

    # Turn off all pixels
    def clear(self):
        self.pixels.fill((0, 0, 0))
        time.sleep(2)
