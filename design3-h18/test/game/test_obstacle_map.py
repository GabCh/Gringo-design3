import unittest

import numpy as np

from atlas.game.obstacle_map import ObstacleMap
from atlas.vision.util import WorldCoordinate


class ObstacleMapTest(unittest.TestCase):

    def setUp(self):
        self.obstacle_map = ObstacleMap(np.zeros((100, 100, 1), dtype='bool'))

    def test_givenTileNotSurroundedByWalls_whenGettingNeighbours_thenReturnAllFourDirectlyConnectedTiles(self):
        neighbours = self.obstacle_map.get_neighbours(50, 50)

        self.assertEqual(4, len(neighbours))

    def test_givenOriginTile_whenGettingNeighbours_thenReturnTwoPositiveNeighbours(self):
        neighbours = self.obstacle_map.get_neighbours(0, 0)

        self.assertEqual(2, len(neighbours))

    def test_givenTileSurroundedByWalls_whenGettingNeighbours_thenReturnNoNeighbours(self):
        self.obstacle_map = ObstacleMap(np.ones((100, 100, 1), dtype='bool'))

        neighbours = self.obstacle_map.get_neighbours(50, 50)

        self.assertEqual(0, len(neighbours))

    def test_whenGettingTileCorrespondingToWorldCoordinate_thenCalculatesUsingHardcoded1cmRatio(self):
        coordinate = WorldCoordinate(3.23, 1.10)

        x, y = self.obstacle_map.get_tile_for_world_coordinate(coordinate)

        self.assertEqual(int(coordinate.x * 100), x)
        self.assertEqual(int(coordinate.y * 100), y)

    def test_whenGettingWorldCoordinateCoorrespondingToTile_thenCalculatesUsingHardcoded1cmRatio(self):
        coordinate = (50, 50)

        world_coordinate = self.obstacle_map.get_world_coordinate_for_tile(*coordinate)

        self.assertAlmostEqual(coordinate[0] / 100.0, world_coordinate.x)
        self.assertAlmostEqual(coordinate[1] / 100.0, world_coordinate.y)


if __name__ == '__main__':
    unittest.main()
