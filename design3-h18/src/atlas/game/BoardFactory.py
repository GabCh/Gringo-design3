import time
import math
from typing import List

from atlas.game.Cube import CubeColour, Cube
from atlas.game.CubeStorage import CubeStorage
from atlas.game.board import Board
from atlas.game.board_elements import Robot, Obstacle, TargetZone
from atlas.game.element_detectors import BlockLocator, RobotLocator, ObstacleLocator, TargetZoneLocator
from atlas.game.game_status import GameStatus
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.infrastructure.stream import Stream
from atlas.logging import LoggerFactory
from atlas.vision.coordinates import CoordinateTranslator
from atlas.vision.image_repository import ImageRepository
from atlas.vision.util import OrientedWorldCoordinate, PixelCoordinate, OrientedPixelCoordinate

MAX_RETRIES = 5


class BoardFactory(object):
    def create_board(self) -> Board:
        raise NotImplementedError


class VisionBoardFactory(BoardFactory):
    LOGGER = LoggerFactory.get_logger("VisionBoardFactory")

    def __init__(self, image_repository: ImageRepository, block_locator: BlockLocator, robot_locator: RobotLocator,
                 obstacle_locator: ObstacleLocator, coordinate_translator: CoordinateTranslator,
                 objective_flag_container: ObjectiveFlagContainer, target_zone_locator: TargetZoneLocator,
                 game_status: GameStatus):
        self.game_status = game_status
        self.target_zone_locator = target_zone_locator
        self.obstacle_locator = obstacle_locator
        self.coordinate_translator = coordinate_translator
        self.robot_locator = robot_locator
        self.block_locator = block_locator
        self.image_repository = image_repository
        self.objective_flag_container = objective_flag_container

    def create_board(self) -> Board:
        # time.sleep(1.5)
        for i in range(0, MAX_RETRIES):
            cubes = []

            image = self.image_repository.get_next_image()
            cube_pixel_coordinates = {}

            cubes_outside_the_cube_storage = []

            for colour in CubeColour.values():
                pixel_coordinates = self.block_locator.locate_blocks(image, colour)
                cube_pixel_coordinates[colour] = pixel_coordinates
                positions = [x for x in
                             map(lambda pixel: self.coordinate_translator.pixel_to_world(pixel, height=8),
                                 pixel_coordinates)]
                found_cubes = [x for x in map(lambda pos: Cube(pos, colour), positions)]
                cubes_inside_the_cube_storage = Stream(found_cubes).filter(lambda c: c.is_in_cube_storage())
                # TODO remove or tweak this sanity check
                cubes_outside_the_cube_storage.extend(Stream(found_cubes).filter(lambda c: not c.is_in_cube_storage()))
                cubes.extend(found_cubes)

            robot_pixel_coordinates = self.robot_locator.locate_robot(image)
            robot = Robot(
                OrientedWorldCoordinate(self.coordinate_translator.pixel_to_world(robot_pixel_coordinates.coordinate,
                                                                                  height=30),
                                        robot_pixel_coordinates.angle))

            if robot.position.x < -0.5 or robot.position.y < -0.5 and i < MAX_RETRIES - 1:
                self.LOGGER.error("Did not detect the robot. Trying to create a new board.")
                time.sleep(1.5)
                continue

            # cubes_far_from_the_robot = Stream(cubes).filter(
            #     lambda c: not c.position.is_close(robot.position, delta=0.50)).toList()

            obstacle_pixel_coordinates = self.obstacle_locator.locate_obstacles(image)
            obstacle_positions = map(lambda pixel: self.coordinate_translator.pixel_to_world(pixel, height=40),
                                     obstacle_pixel_coordinates)
            obstacles = Stream(obstacle_positions).map(lambda position: Obstacle(position)).toList()

            # TODO Add black blocks outside the cube storage as obstacles for demo3 REMOVE THIS
            # obstacles.extend(Stream(cubes_outside_the_cube_storage).filter(lambda c: c.colour == CubeColour.BLACK).map(
            #     lambda c: Obstacle(c.position)))

            target_zones = Stream(self.target_zone_locator.locate_target_zones(image)).map(
                lambda position: TargetZone(position)).toList()

            board = Board(robot, CubeStorage(cubes), obstacles, self.objective_flag_container,
                          target_zones)

            self.update_vision_game_status(robot_pixel_coordinates, obstacle_pixel_coordinates, cube_pixel_coordinates)
            self.update_logical_game_status(board)

            return board

    def update_vision_game_status(self, robot_coordinate: OrientedPixelCoordinate,
                                  obstacle_coordinates: List[PixelCoordinate], cubes: dict):
        cube_data = []
        for colour, cube_list in cubes.items():
            cube_data.extend([{"x": cube.x, "y": cube.y, "colour": colour} for cube in cube_list])
        if 'vision' not in self.game_status:
            self.game_status['vision'] = {}
        vision_object = {
            "robot": {
                "x": robot_coordinate.coordinate.x,
                "y": robot_coordinate.coordinate.y,
                "angle": robot_coordinate.angle
            },
            "obstacles": [{"x": obstacle.x, "y": obstacle.y} for obstacle in obstacle_coordinates],
            "cubes": cube_data,
            "path": self.game_status['vision'].get('path')
        }
        self.game_status['vision'] = vision_object
        self.game_status.update_robot_actual_position_in_path(robot_coordinate.coordinate)

    def update_logical_game_status(self, board: Board):
        self.game_status['robot'] = {"position": board.robot.position.__dict__, "angle": board.robot.angle}
        self.game_status['cubes'] = [x for x in map(lambda c: {"position": c.position.__dict__, "colour": c.colour},
                                                    board.cubeStorage.cubes)]
        self.game_status['obstacles'] = [x for x in map(lambda o: {"position": o.position.__dict__}, board.obstacles)]
        flag = board.objective_flag_container.get()
        if flag is not None:
            self.game_status['flag'] = {"visual": flag.pattern, "name": flag.country_name, "number": flag.flag_code}
