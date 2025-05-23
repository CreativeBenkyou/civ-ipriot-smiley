import time
from blinkable import Blinkable
from smiley import Smiley


class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()
        self.draw_eyebrows()

    def draw_eyebrows(self):
        """
        Draws the eyebrows feature on a smiley
        """
        eyebrows = [9, 18, 14, 21]
        for pixel in eyebrows:
            self.pixels[pixel] = self.BLANK

    def draw_mouth(self):
        """
        Draws the mouth feature on a smiley
        """
        mouth = [42, 43, 44, 45, 49, 54]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        """
        Draws open or closed eyes on a smiley
        :param wide_open: Render eyes wide open or shut
        """

        eyes = [26, 29]
        for pixel in eyes:
            self.pixels[pixel] = self.BLANK if wide_open else self.complexion()

    def blink(self, delay=0.25):
        """
       Blinks the smiley's eyes once

        :param delay: Delay between blinks (in seconds)
        """
        self.draw_eyes(wide_open=False)
        self.show()
        time.sleep(delay)
        self.draw_eyes(wide_open=True)
        self.show()