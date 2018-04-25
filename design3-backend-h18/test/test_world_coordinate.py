import unittest

import math

from atlas.vision.util import WorldDelta


class WorldCoordinateTest(unittest.TestCase):

    def test_givenWorldDelta_whenGettingAngle_thenReturnAngleInRadians(self):
        world_delta = WorldDelta(1, 1)
        result = world_delta.angle_radians()
        expected = math.radians(135 + 360)
        self.assertAlmostEqual(expected, result)

    def test_givenAngleInThirdQuadrant_whenGettingDeltaAngle_thenReturnPositiveAngleInRadians(self):
        world_delta = WorldDelta(-1, -1)
        result = world_delta.angle_radians()
        expected = math.radians(270 + 45)
        self.assertAlmostEqual(expected, result)

