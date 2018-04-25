from typing import List

import atlas.game.directions as directions
from atlas.game.board_elements import Localizable
from atlas.vision.util import WorldCoordinate, OrientedWorldCoordinate


class Cube(Localizable):
    Y_BOUNDARY_CLOSE_TO_WESTERN_WALL = 2.1
    Y_BOUNDARY_CLOSE_TO_CUBE_STORAGE = 1.75
    X_BOUNDARY_CLOSE_TO_NORTHERN_WALL = 1
    X_BOUNDARY_CLOSE_TO_SOUTHERN_WALL = 0.12

    def __init__(self, position: WorldCoordinate, colour: int):
        Localizable.__init__(self, position)
        self.colour = colour

    def get_grab_orientation(self) -> int:
        if self.position.y > self.Y_BOUNDARY_CLOSE_TO_WESTERN_WALL:
            return directions.FACING_WEST
        if self.position.x > self.X_BOUNDARY_CLOSE_TO_NORTHERN_WALL:
            return directions.FACING_NORTH
        if self.position.x < self.X_BOUNDARY_CLOSE_TO_SOUTHERN_WALL:
            return directions.FACING_SOUTH
        raise CubeNotAgainstWallException()

    def get_grab_position(self) -> OrientedWorldCoordinate:
        orientation = self.get_grab_orientation()
        approach_position = None
        if orientation == directions.FACING_WEST:
            approach_position = WorldCoordinate(self.position.x, self.position.y - 0.30)
        elif orientation == directions.FACING_NORTH:
            approach_position = WorldCoordinate(self.position.x - 0.30, self.position.y)
        elif orientation == directions.FACING_SOUTH:
            approach_position = WorldCoordinate(self.position.x + 0.30, self.position.y)

        return OrientedWorldCoordinate(approach_position, orientation)

    def is_in_cube_storage(self) -> bool:
        return self.position.y > self.Y_BOUNDARY_CLOSE_TO_CUBE_STORAGE


class CubeColour:
    RED = 0
    YELLOW = 1
    BLUE = 2
    GREEN = 3
    BLACK = 4
    WHITE = 5

    NONE = 99

    @staticmethod
    def from_string(string: str) -> int:
        if string == "RED":
            return CubeColour.RED
        if string == "YELLOW":
            return CubeColour.YELLOW
        if string == "BLUE":
            return CubeColour.BLUE
        if string == "GREEN":
            return CubeColour.GREEN
        if string == "BLACK":
            return CubeColour.BLACK
        if string == "WHITE":
            return CubeColour.WHITE
        if string == "":
            return CubeColour.NONE
        raise InvalidCubeColourException(string)

    @staticmethod
    def to_string(enum: int) -> str:
        if enum == CubeColour.RED:
            return "RED"
        if enum == CubeColour.YELLOW:
            return "YELLOW"
        if enum == CubeColour.BLUE:
            return "BLUE"
        if enum == CubeColour.GREEN:
            return "GREEN"
        if enum == CubeColour.BLACK:
            return "BLACK"
        if enum == CubeColour.WHITE:
            return "WHITE"
        if enum == CubeColour.NONE:
            return ""
        raise InvalidCubeColourException(enum)

    @staticmethod
    def values() -> List[int]:
        return [CubeColour.RED, CubeColour.YELLOW, CubeColour.BLUE, CubeColour.GREEN, CubeColour.BLACK,
                CubeColour.WHITE]


class CubeNotAgainstWallException(Exception):
    pass


class InvalidCubeColourException(Exception):
    pass
