from typing import List

from atlas.game.CubeStorage import CubeStorage
from atlas.game.board_elements import Robot, Obstacle, TargetZone
from atlas.game.board_mapper import BoardMapper
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.game.obstacle_map import ObstacleMap


class Board(object):

    def __init__(self, robot: Robot, cube_storage: CubeStorage, obstacles: List[Obstacle],
                 objective_flag_container: ObjectiveFlagContainer, target_zones: List[TargetZone]):
        self.obstacles = obstacles
        self.cubeStorage = cube_storage
        self.robot = robot
        self.objective_flag_container = objective_flag_container
        self.targetZones = target_zones
        self.width = 231
        self.height = 111

    def get_obstacle_map(self, obstacle_diameter: int = 12, cube_width: int = 8, border_width: int = 5,
                         cube_storage_border: int = 5, cube_storage_lenght: int = 50) -> ObstacleMap:
        board_mapper = BoardMapper()
        return board_mapper.generate(self, obstacle_diameter, cube_width, border_width,
                                     cube_storage_lenght, cube_storage_border)

    def get_x_width(self) -> float:
        # TODO check with GabC that this is a good value
        return 1.11

    def get_y_length(self) -> float:
        return 2.31
