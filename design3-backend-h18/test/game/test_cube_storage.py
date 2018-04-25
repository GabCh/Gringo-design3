import unittest

from atlas.game.Cube import Cube, CubeColour
from atlas.game.CubeStorage import CubeStorage, NoSuchCubeException
from atlas.vision.util import WorldCoordinate, OrientedWorldCoordinate


class CubeStorageTest(unittest.TestCase):
    SOME_POSITION = WorldCoordinate(3, -5)
    CUBE_COLOUR = CubeColour.RED
    SOME_ORIENTATION = 43

    NO_SUCH_CUBE_COLOUR = CubeColour.BLACK
    INACCESSIBLE_POSITION = WorldCoordinate(100, 100)

    def setUp(self):
        self.cubeMock = Cube(self.SOME_POSITION, self.CUBE_COLOUR)
        self.cubeMock.get_grab_position = lambda: OrientedWorldCoordinate(self.SOME_POSITION, self.SOME_ORIENTATION)

        self.cubes = [self.cubeMock]
        self.cubeStorage = CubeStorage(self.cubes)

    def test_givenNoCubeWithCorrespondingColour_whenGettingCube_thenThrowNoSuchCubeException(self):
        with self.assertRaises(NoSuchCubeException):
            self.cubeStorage.get_cube_position(self.NO_SUCH_CUBE_COLOUR)

    def test_givenAdmissibleCube_whenGettingCube_thenReturnAllCubesInAList(self):
        cubes = self.cubeStorage.get_cube_position(self.CUBE_COLOUR)

        self.assertEqual(1, len(cubes))
        self.assertAlmostEqual(self.SOME_POSITION.x, cubes[0].coordinate.x)
        self.assertAlmostEqual(self.SOME_POSITION.y, cubes[0].coordinate.y)


if __name__ == '__main__':
    unittest.main()
