import math
import time
from typing import List

from atlas.game.BoardFactory import BoardFactory
from atlas.game.Cube import Cube
from atlas.game.Task import Task
from atlas.game.game_status import GameStatus
from atlas.infrastructure.stream import Stream
from atlas.logging import LoggerFactory
from atlas.pathfinder.pathplanner import PathPlanner
from atlas.vision.coordinates import CoordinateTranslator
from atlas.vision.util import OrientedWorldCoordinate, WorldCoordinate


class GoToTask(Task):
    LOGGER = LoggerFactory.get_logger("GoToTask")

    def __init__(self, path_planner: PathPlanner, board_factory: BoardFactory, game_status: GameStatus,
                 coordinate_translator: CoordinateTranslator, task_factory: "TaskFactory",
                 destination: OrientedWorldCoordinate):
        print("destination:{},{}".format(destination.coordinate.x, destination.coordinate.y))
        self.task_factory = task_factory
        self.destination = destination
        self.path_planner = path_planner
        self.board_factory = board_factory
        self.game_status = game_status
        self.coordinate_translator = coordinate_translator

    def run(self):
        board = self.board_factory.create_board()
        waypoints = self.path_planner.plan(board.robot.position, self.destination.coordinate, board)
        self.update_planned_path_in_game_status(waypoints)

        self.follow_path(waypoints)

    def follow_path(self, waypoints: List[WorldCoordinate]):
        for i, point in enumerate(waypoints[:-2]):
            next_point = waypoints[i + 1]
            time.sleep(1)
            board = self.board_factory.create_board()
            self.follow_step(board.robot.position, next_point)

            if not board.robot.position.is_close(next_point, delta=0.02):
                self.LOGGER.info("Far from waypoint, realigning...")
                self.task_factory.create_task("realign", **{"x": next_point.x, "y": next_point.y}).run()

        # Realign for last move
        if waypoints[-1].y > waypoints[-2].y:
            self.orient_robot_to(self.destination.angle)
            self.task_factory.create_task("realign", **{"x": waypoints[-1].x, "y": waypoints[-1].y}).run()
        else:
            self.follow_step(waypoints[-2], waypoints[-1])
            self.orient_robot_to(self.destination.angle)

    def orient_robot_to(self, final_angle: int):
        # First move is crude, second confirms the alignment
        self.task_factory.create_task("orient_to", **{"angle": final_angle}).run()
        self.task_factory.create_task("orient_to", **{"angle": final_angle}).run()

    def follow_step(self, current_position: WorldCoordinate, next_position: WorldCoordinate):
        self.LOGGER.debug("currently at {},{}".format(current_position.x, current_position.y))
        self.LOGGER.debug("going at {},{}".format(next_position.x, next_position.y))
        distance = next_position - current_position
        angle = int(math.degrees(distance.angle_radians()) % 360)
        if distance.length() < 0.35:
            self.task_factory.create_task("realign", **{"x": next_position.x, "y": next_position.y}).run()
        else:
            self.orient_robot_to(angle)
            self.task_factory.create_task("move_forward", **{"distance": distance.length()}).run()

    def update_planned_path_in_game_status(self, path: List[WorldCoordinate]):
        pixel_path = Stream(path).map(
            lambda coordinate: self.coordinate_translator.world_to_pixel(coordinate)).toList()

        self.game_status.set_new_path(pixel_path)
