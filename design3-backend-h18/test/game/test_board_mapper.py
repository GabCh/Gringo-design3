import random
import unittest
import numpy as np

from atlas.game.board import Board
from atlas.game.board_elements import Robot, Obstacle, TargetZone
from atlas.game.Cube import Cube, CubeColour
from atlas.game.CubeStorage import CubeStorage
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.vision.util import OrientedWorldCoordinate, WorldCoordinate


class BoardMapperTest(unittest.TestCase):

    @staticmethod
    def create_board():
        robot = Robot(OrientedWorldCoordinate(WorldCoordinate(random.uniform(0.0, 1.11), random.uniform(0.0, 2.31)),
                                              random.randint(0, 360)))
        obstacles = []
        for i in range(2):
            obstacles.append(Obstacle(WorldCoordinate(random.uniform(0.0, 1.11), random.uniform(0.0, 2.31))))

        cubes = []
        for i in range(5):
            cubes.append(Cube(WorldCoordinate(random.uniform(0.0, 1.11), random.uniform(0.0, 2.31)),
                              CubeColour.values()[random.randint(0, 5)]))
        cube_storage = CubeStorage(cubes)

        flag_container = ObjectiveFlagContainer()

        target_zones = [x for x in map(lambda position: TargetZone(position),
                                       HardcodedTargetZoneLocator().locate_target_zones(np.zeros((1280, 720))))]

        board = Board(robot, cube_storage, obstacles, flag_container, target_zones)
        return board

    def test_givenBoard_whenGeneratingObstacleMap_thenMapCorrectly(self):

        board = self.create_board()
        board_map = board.get_obstacle_map()

        for obstacle in board.obstacles:
            self.assertTrue(board_map.is_obstacle(int(obstacle.position.x * 100),
                                                  int(obstacle.position.y * 100)))

        for cube in board.cubeStorage.cubes:
            self.assertTrue(board_map.is_obstacle(int(cube.position.x*100),
                                                  int(cube.position.y*100)))

    def test_givenBoard_whenGeneratingObstacleMapWithInflate_thenMapCorrectly(self):

        board = self.create_board()
        board_map = board.get_obstacle_map()

        for obstacle in board.obstacles:
            self.assertTrue(board_map.is_obstacle(int(obstacle.position.x * 100),
                                                  int(obstacle.position.y * 100)))

        for cube in board.cubeStorage.cubes:
            self.assertTrue(board_map.is_obstacle(int(cube.position.x * 100),
                                                  int(cube.position.y * 100)))

    def test_givenBoard_whenGeneratingObstacleMap_thenMapBordersCorrectly(self):

        board = self.create_board()
        board_map = board.get_obstacle_map()

        self.assertTrue(board_map.is_obstacle(int(0 + random.uniform(0, 5)),
                                              int(0 + random.uniform(0, 5))))  # upper left corner
        self.assertTrue(board_map.is_obstacle(int(board_map.height - random.uniform(0, 5)),
                                              int(board_map.width - random.uniform(0, 5))))  # lower right corner


if __name__ == '__main__':
    unittest.main()
