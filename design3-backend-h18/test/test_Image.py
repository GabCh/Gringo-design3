import unittest

import numpy as np

from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate


class ImageTest(unittest.TestCase):
    WIDTH = 20
    HEIGHT = 20

    def setUp(self):
        self.image = Image(np.zeros((self.WIDTH, self.HEIGHT)))

    def test_givenPixelWithNegativeCoordinates_whenCheckingIsInside_thenPixelIsNotInside(self):
        negativePixel = PixelCoordinate(-1, 1)

        result = self.image.contains(negativePixel)

        self.assertFalse(result)

    def test_givenPixelWithOverflowingX_whenCheckingIsInside_thenPixelIsNotInside(self):
        overflowingXPixel = PixelCoordinate(self.WIDTH + 1, self.HEIGHT - 1)

        result = self.image.contains(overflowingXPixel)

        self.assertFalse(result)

    def test_givenPixelAtWidthHeightCorner_whenCheckingIsInside_thenPixelIsNotInside(self):
        pixelOnBorder = PixelCoordinate(self.WIDTH, self.HEIGHT)

        result = self.image.contains(pixelOnBorder)

        self.assertFalse(result)

    def test_givenPixelInCenter_whenCheckingIsInside_thenPixelIsInside(self):
        centerPixel = PixelCoordinate(self.WIDTH // 2, self.HEIGHT // 2)

        result = self.image.contains(centerPixel)

        self.assertTrue(result)

