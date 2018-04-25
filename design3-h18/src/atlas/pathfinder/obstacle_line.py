from typing import List

from atlas.game.board_elements import Obstacle
from atlas.infrastructure.stream import Stream
from atlas.pathfinder.node import Node
from atlas.vision.util import WorldCoordinate

BOARD_X_WIDTH = 1.11
ROBOT_WIDTH = 0.32


class ObstacleLine(object):

    def __init__(self, obstacle: Obstacle):
        self.obstacle = obstacle
        self.y = self.obstacle.position.y
        self.neighbouringObstacles = []

    def is_close(self, other: "ObstacleLine", delta=0.20) -> bool:
        return abs(self.y - other.y) < delta

    def add_neighbouring_obstacle(self, neighbour: "ObstacleLine"):
        if self.is_close(neighbour):
            self.neighbouringObstacles.append(neighbour.obstacle)

    def has_to_be_crossed_to_go_to_goal(self, start: WorldCoordinate, goal: WorldCoordinate) -> bool:
        return start.y < self.y < goal.y or start.y > self.y > goal.y

    def get_ways_across(self) -> List[Node]:
        obstacle_points = [self.obstacle.position.x] + [obstacle.position.x for obstacle in self.neighbouringObstacles]
        obstacle_points.sort()
        separators = [0.0] + obstacle_points + [BOARD_X_WIDTH]
        spaces = [separators[i + 1] - separators[i] for i in range(0, len(separators) - 1)]

        ways_across = []
        for i, space in enumerate(spaces):
            if space > ROBOT_WIDTH:
                ways_across.append(WorldCoordinate(separators[i] + space / 2, self.y))

        return Stream(ways_across).map(lambda coordinate: Node(coordinate)).toList()
