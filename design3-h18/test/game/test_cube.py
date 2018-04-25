import unittest

from atlas.game.Cube import Cube, CubeColour, CubeNotAgainstWallException
from atlas.vision.util import WorldCoordinate
import atlas.game.directions as directions


class CubeTest(unittest.TestCase):
    POSITION_AGAINST_NORTHERN_WALL = WorldCoordinate(1.06, 1)
    POSITION_AGAINST_WEST_WALL = WorldCoordinate(0.75, 2.22)
    POSITION_AGAINST_SOUTH_WALL = WorldCoordinate(0.03, 1.7)
    POSITION_NOT_AGAINST_ANY_WALL = WorldCoordinate(1, 1)

    SOME_COLOUR = CubeColour.RED

    def test_givenCubeAlongNorthernWall_whenGettingGrabAngle_thenReturnNorth(self):
        cube = Cube(self.POSITION_AGAINST_NORTHERN_WALL, self.SOME_COLOUR)

        grab_orientation = cube.get_grab_orientation()

        self.assertEqual(directions.FACING_NORTH, grab_orientation)

    def test_givenCubeAlongEasternWall_whenGettingGrabAngle_thenReturnEast(self):
        cube = Cube(self.POSITION_AGAINST_WEST_WALL, self.SOME_COLOUR)

        grab_orientation = cube.get_grab_orientation()

        self.assertEqual(directions.FACING_WEST, grab_orientation)

    def test_givenCubeAlongSouthernWall_whenGettingGrabAngle_thenReturnSouth(self):
        cube = Cube(self.POSITION_AGAINST_SOUTH_WALL, self.SOME_COLOUR)

        grab_orientation = cube.get_grab_orientation()

        self.assertEqual(directions.FACING_SOUTH, grab_orientation)

    def test_givenCubeFarFromAnyWall_whenGettingGrabAngle_thenThrowCubeNotAgainstWallException(self):
        cube = Cube(self.POSITION_NOT_AGAINST_ANY_WALL, self.SOME_COLOUR)

        with self.assertRaises(CubeNotAgainstWallException):
            cube.get_grab_orientation()

    def test_givenCubeAlongNorthernWall_whenGettingGrabPosition_thenReturnPosition10cmSouth(self):
        cube = Cube(self.POSITION_AGAINST_NORTHERN_WALL, self.SOME_COLOUR)

        position = cube.get_grab_position()

        self.assertAlmostEqual(self.POSITION_AGAINST_NORTHERN_WALL.x - 0.3, position.coordinate.x)
        self.assertAlmostEqual(self.POSITION_AGAINST_NORTHERN_WALL.y, position.coordinate.y)

    def test_givenCubeAlongSouthernWall_whenGettingGrabPosition_thenReturnPosition10cmNorth(self):
        cube = Cube(self.POSITION_AGAINST_SOUTH_WALL, self.SOME_COLOUR)

        position = cube.get_grab_position()

        self.assertAlmostEqual(self.POSITION_AGAINST_SOUTH_WALL.x + 0.3, position.coordinate.x)
        self.assertAlmostEqual(self.POSITION_AGAINST_SOUTH_WALL.y, position.coordinate.y)

    def test_givenCubeAlongWesternWall_whenGettingGrabPosition_thenReturnPosition10cmEast(self):
        cube = Cube(self.POSITION_AGAINST_WEST_WALL, self.SOME_COLOUR)

        position = cube.get_grab_position()

        self.assertAlmostEqual(self.POSITION_AGAINST_WEST_WALL.x, position.coordinate.x)
        self.assertAlmostEqual(self.POSITION_AGAINST_WEST_WALL.y - 0.3, position.coordinate.y)


if __name__ == '__main__':
    unittest.main()
