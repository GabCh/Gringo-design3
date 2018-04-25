import unittest

from atlas.vision.util import PixelCoordinate


class PixelCoordinateTest(unittest.TestCase):
    SOME_X = 5
    SOME_Y = 10

    def test_whenGettingNorth_thenReturnPixelWithLowerYCoordinate(self):
        pixel = PixelCoordinate(self.SOME_X, self.SOME_Y)

        north = pixel.north()

        self.assertEqual(pixel.x, north.x)
        self.assertEqual(pixel.y -1, north.y)

    def test_whenGettingSouth_thenReturnPixelWithHigherYCoordinate(self):
        pixel = PixelCoordinate(self.SOME_X, self.SOME_Y)

        south = pixel.south()

        self.assertEqual(pixel.x, south.x)
        self.assertEqual(pixel.y + 1, south.y)

