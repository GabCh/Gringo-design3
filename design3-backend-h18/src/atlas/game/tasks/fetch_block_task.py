import time

from atlas.game import directions
from atlas.game.BoardFactory import BoardFactory
from atlas.game.Cube import CubeColour
from atlas.game.CubeStorage import NoSuchCubeException
from atlas.game.Task import Task
from atlas.game.board import Board
from atlas.game.flag import CubeRequest
from atlas.game.game_status import GameStatus
from atlas.logging import LoggerFactory
from atlas.pathfinder.tree_walker import CannotFindPathException
from atlas.vision.util import OrientedWorldCoordinate

MAX_RETRIES = 3


class FetchBlockTask(Task):
    LOGGER = LoggerFactory.get_logger("FetchBlockTask")

    def __init__(self, board_factory: BoardFactory, game_status: GameStatus, task_factory: "TaskFactory",
                 cube_request: CubeRequest):
        self.task_factory = task_factory
        self.game_status = game_status
        self.board_factory = board_factory
        self.cubeRequest = cube_request

    def run(self):
        self.task_factory.create_task("release").run()
        self.game_status.set_next_colour(self.cubeRequest.blockColour)

        board = self.board_factory.create_board()
        for i in range(0, MAX_RETRIES):
            try:
                cube_positions = board.cubeStorage.get_cube_position(self.cubeRequest.blockColour)
                break
            except NoSuchCubeException:
                self.LOGGER.warn("Did not find cube {}".format(CubeColour.to_string(self.cubeRequest.blockColour)))
                time.sleep(1)
                board = self.board_factory.create_board()
                continue

        accessible_cubes = [x for x in filter(lambda x: self.__is_accessible(x, board), cube_positions)]
        if len(accessible_cubes) == 0:
            self.LOGGER.error("Cannot find an accessible cube.")
            raise NoAccessibleCubeException()

        target_cube = accessible_cubes[0]
        try:
            self.task_factory.create_task("goto", **{"x": target_cube.coordinate.x, "y": target_cube.coordinate.y,
                                                     "angle": target_cube.angle}).run()
        except CannotFindPathException:
            self.task_factory.create_task("realign", **{"x": 0.5, "y": board.robot.position.y}).run()
            self.task_factory.create_task("goto", **{"x": target_cube.coordinate.x, "y": target_cube.coordinate.y,
                                                     "angle": target_cube.angle}).run()

        self.task_factory.create_task("realign",
                                      **{"x": target_cube.coordinate.x, "y": target_cube.coordinate.y}).run()
        self.task_factory.create_task("realign",
                                      **{"x": target_cube.coordinate.x, "y": target_cube.coordinate.y}).run()

        self.task_factory.create_task("move_forward", **{"distance": 0.11}).run()

        self.task_factory.create_task("grab").run()

        self.task_factory.create_task("move_forward", **{"distance": -0.13}).run()
        try:
            self.task_factory.create_task("goto",
                                          **{"x": self.cubeRequest.drop_position.x,
                                             "y": self.cubeRequest.drop_position.y,
                                             "angle": directions.FACING_EAST}).run()
        except CannotFindPathException:
            self.task_factory.create_task("realign", **{"x": 0.5, "y": 1.1}).run()
            self.task_factory.create_task("goto",
                                          **{"x": self.cubeRequest.drop_position.x,
                                             "y": self.cubeRequest.drop_position.y,
                                             "angle": directions.FACING_EAST}).run()

        self.task_factory.create_task("realign",
                                      **{"x": self.cubeRequest.drop_position.x,
                                         "y": self.cubeRequest.drop_position.y}).run()
        self.task_factory.create_task("realign",
                                      **{"x": self.cubeRequest.drop_position.x,
                                         "y": self.cubeRequest.drop_position.y}).run()

        self.task_factory.create_task("release").run()

        self.task_factory.create_task("move_forward", **{"distance": -0.13}).run()

    def __is_accessible(self, cube_approach_position: OrientedWorldCoordinate, board: Board) -> bool:
        obstacle_map = board.get_obstacle_map()
        tile = obstacle_map.get_tile_for_world_coordinate(cube_approach_position.coordinate)
        return not obstacle_map.is_obstacle(*tile)


class NoAccessibleCubeException(Exception):
    pass
