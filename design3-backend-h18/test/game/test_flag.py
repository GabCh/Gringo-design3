import unittest

from atlas.game.board_elements import TargetZone
from atlas.vision.util import WorldCoordinate
from atlasTesting.testing_flag import CANADIAN_FLAG


class FlagTest(unittest.TestCase):
    TARGET_ZONES = [TargetZone(WorldCoordinate(t, t)) for t in range(0, 9)]

    def setUp(self):
        self.flagWithEmptySpaces = CANADIAN_FLAG

    def test_givenFlagWithEmptySpaces_whenGettingCubeRequests_thenReturnCubeRequestForEachNonEmptySquare(self):
        cube_requests = self.flagWithEmptySpaces.get_cube_requests(self.TARGET_ZONES)

        self.assertEqual(3, len(cube_requests))


if __name__ == '__main__':
    unittest.main()
