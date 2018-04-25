from typing import List

from atlas.game.Cube import CubeColour, CubeNotAgainstWallException, Cube
from atlas.vision.util import OrientedWorldCoordinate


class CubeStorage(object):

    def __init__(self, cubes: List[Cube]):
        self.cubes = cubes

    def get_cube_position(self, cube_colour: CubeColour) -> List[OrientedWorldCoordinate]:
        cube_positions = []
        for cube in self.cubes:
            if cube.colour == cube_colour:
                try:
                    cube_positions.append(cube.get_grab_position())
                except CubeNotAgainstWallException:
                    continue
        if len(cube_positions) == 0:
            raise NoSuchCubeException(cube_colour)
        return cube_positions


class NoSuchCubeException(Exception):
    pass
