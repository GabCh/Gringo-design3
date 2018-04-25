from typing import List

from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate, OrientedPixelCoordinate, WorldCoordinate


class BlockLocator(object):

    def locate_blocks(self, image: Image, cube_colour: int) -> List[PixelCoordinate]:
        raise NotImplementedError


class RobotLocator(object):

    def locate_robot(self, image: Image) -> OrientedPixelCoordinate:
        raise NotImplementedError


class ObstacleLocator(object):

    def locate_obstacles(self, image: Image) -> List[PixelCoordinate]:
        raise NotImplementedError


class TargetZoneLocator(object):

    def locate_target_zones(self, image: Image) -> List[WorldCoordinate]:
        raise NotImplementedError


class TableLocator(object):

    def locate_table(self, image: Image) -> List[PixelCoordinate]:
        raise NotImplementedError
