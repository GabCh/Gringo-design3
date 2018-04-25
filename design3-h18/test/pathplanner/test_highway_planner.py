import unittest
from unittest import mock

from atlas.game.board import Board
from atlas.game.board_elements import Obstacle
from atlas.pathfinder.highway_planner import HighwayPlanner
from atlas.pathfinder.orthogonal_projection_calculator import OrthogonalProjectionCalculator
from atlas.pathfinder.tree_walker import TreeWalker
from atlas.vision.util import WorldCoordinate


class HighwayPlannerTest(unittest.TestCase):

    def setUp(self):
        self.planner = HighwayPlanner(OrthogonalProjectionCalculator(), TreeWalker())

    def test_givenObstacleBetweenTwoNodes_whenCheckingHasLineOfSight_thenNodesDoNotHaveLineOfSight(self):
        a_node = WorldCoordinate(1, 1)
        a_second_node = WorldCoordinate(3, 3)
        an_obstacle = Obstacle(WorldCoordinate(2, 2))
        board_mock = mock.create_autospec(Board)
        board_mock.obstacles = [an_obstacle]

        has_line_of_sight = self.planner.has_line_of_sight(a_node, a_second_node, board_mock)

        self.assertFalse(has_line_of_sight)

    def test_givenAnObstacleNotBetweenTheTwoNodes_whenCheckingHasLineOfSight_thenNodesDoHaveLineOfSight(self):
        a_node = WorldCoordinate(1, 1)
        a_second_node = WorldCoordinate(3, 3)
        an_obstacle = Obstacle(WorldCoordinate(5, 5))
        board_mock = mock.create_autospec(Board)
        board_mock.obstacles = [an_obstacle]

        has_line_of_sight = self.planner.has_line_of_sight(a_node, a_second_node, board_mock)

        self.assertTrue(has_line_of_sight)
