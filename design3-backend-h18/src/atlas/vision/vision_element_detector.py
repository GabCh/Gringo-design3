from typing import List

import atlas.logging.LoggerFactory as LoggerFactory
from atlas.game.Cube import CubeColour
from atlas.game.element_detectors import BlockLocator, RobotLocator, ObstacleLocator, TableLocator, TargetZoneLocator
from atlas.vision.image import Image
from atlas.vision.block_detector import detect_block
from atlas.vision.colourrange import ColourRange
from atlas.vision.obstacle_detector import detect_obstacle
from atlas.vision.robot_detector import detect_robot
from atlas.vision.table_cropper import crop_to_table_by_contours
from atlas.vision.goal_area_detector import detect_green_zone
from atlas.vision.util import PixelCoordinate, OrientedPixelCoordinate


class VisionBlockLocator(BlockLocator):

    LOGGER = LoggerFactory.get_logger("VisionBlockLocator")

    def locate_blocks(self, image: Image, cube_colour: int) -> List[PixelCoordinate]:
        blocks = detect_block(image, ColourRange.translate_to_colour_range(cube_colour))
        if blocks:
            return blocks
        else:
            self.LOGGER.debug("No " + CubeColour.to_string(cube_colour) + " blocks detected")
            return blocks


class VisionRobotLocator(RobotLocator):

    LOGGER = LoggerFactory.get_logger("VisionRobotLocator")

    def locate_robot(self, image: Image) -> OrientedPixelCoordinate:
        robot = detect_robot(image)
        if robot:
            return OrientedPixelCoordinate(robot[0], int(robot[1]))
        else:
            self.LOGGER.warn("No robot detected.")
            return OrientedPixelCoordinate(PixelCoordinate(-1, -1), 180)


class VisionObstacleLocator(ObstacleLocator):

    LOGGER = LoggerFactory.get_logger("VisionObstacleLocator")

    def locate_obstacles(self, image: Image) -> List[PixelCoordinate]:
        obstacles = detect_obstacle(image)
        if obstacles:
            return obstacles
        else:
            self.LOGGER.warn("No obstacles detected.")
            return obstacles


class VisionTableLocator(TableLocator):

    LOGGER = LoggerFactory.get_logger("VisionTableLocator")

    def locate_table(self, image: Image) -> List[PixelCoordinate]:
        table = crop_to_table_by_contours(image)
        if table:
            return [PixelCoordinate(table[0], table[1]), PixelCoordinate(table[2], table[3])]
        else:
            self.LOGGER.error("No table detected.")
            return table


class VisionTargetZoneLocator(TargetZoneLocator):

    LOGGER = LoggerFactory.get_logger("VisionTargetZoneLocator")

    def locate_target_zones(self, image: Image) -> List[PixelCoordinate]:
        zone = detect_green_zone(image)
        if zone:
            return zone
        else:
            self.LOGGER.warn("No green-zone detected.")
            return zone
