import unittest

from atlas.game.board_elements import TargetZone
from atlas.vision.util import WorldCoordinate


class TargetZoneTest(unittest.TestCase):
    SOME_POSITION = WorldCoordinate(5, 5)

    def setUp(self):
        self.targetZone = TargetZone(self.SOME_POSITION)

    def test_givenNewTargetZone_whenCheckingIsOccupied_thenIsNotOccupied(self):
        isOccupied = self.targetZone.isOccupied

        self.assertFalse(isOccupied)

    def test_givenOccupiedZone_whenCheckingIsOccupied_thenReturnIsOccupied(self):
        self.targetZone.set_occupied()

        isOccupied = self.targetZone.isOccupied

        self.assertTrue(isOccupied)
