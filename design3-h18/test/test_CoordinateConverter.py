import unittest

from atlas.vision.coordinates import CoordinateTranslator
from atlas.vision.util import PixelCoordinate, WorldCoordinate

ORIGIN = PixelCoordinate(1, 2)
PIXEL_TO_WORLD_SCALE = 0.1  # meters per pixel
WORLD_WIDTH_IN_PIXELS = 8
WORLD_HEIGHT_IN_PIXELS = 5


class ConverterTest(unittest.TestCase):
    def setUp(self):
        self.converter = CoordinateTranslator(WORLD_WIDTH_IN_PIXELS, WORLD_WIDTH_IN_PIXELS * PIXEL_TO_WORLD_SCALE,
                                              ORIGIN)

    def test_whenConvertingPixelsToWorld_thenReturnCorrectlyScaledCoordinate(self):
        some_pixel_coordinate = PixelCoordinate(4, 5)
        expected_coordinate = WorldCoordinate(0.4, 0.5)

        world_coordinate = self.converter.pixel_to_world(some_pixel_coordinate)

        self.assertAlmostEqual(expected_coordinate.x, world_coordinate.x, delta=0.1)
        self.assertAlmostEqual(expected_coordinate.y, world_coordinate.y, delta=0.1)


if __name__ == "__main__":
    unittest.main()