from typing import List

from atlas.game.board import Board
from atlas.game.obstacle_map import ObstacleMap
from atlas.game.path_planner import PathPlanner
from atlas.pathfinder.problem import AtlasSearchProblem, manhattanHeuristic
from atlas.pathfinder.search import aStarSearch
from atlas.vision.util import PixelCoordinate, WorldCoordinate


class AStarPathPlanner(PathPlanner):

    def plan(self, start: WorldCoordinate, goal: WorldCoordinate, board: Board) -> List[WorldCoordinate]:
        obstacle_map = board.get_obstacle_map()
        start_tile = obstacle_map.get_tile_for_world_coordinate(start)
        goal_tile = obstacle_map.get_tile_for_world_coordinate(goal)

        # TODO optimize movements to reduce stuttering
        discrete_path = self._plan_pixels(PixelCoordinate(*start_tile), PixelCoordinate(*goal_tile), obstacle_map)

        return [step for step in map(lambda p: obstacle_map.get_world_coordinate_for_tile(p.x, p.y), discrete_path)]

    def _plan_pixels(self, start: PixelCoordinate, goal: PixelCoordinate, obstacle_map: ObstacleMap) -> List[
        PixelCoordinate]:
        problem = AtlasSearchProblem(start, goal, obstacle_map)

        return aStarSearch(problem, manhattanHeuristic)
