from typing import List

from atlas.game.Cube import CubeColour
from atlas.game.board_elements import TargetZone
from atlas.vision.util import WorldCoordinate


class Flag(object):
    """Stores the flag as a 3x3 matrix of colours."""

    def __init__(self, flag_code: int, pattern: list, country_name: str):
        self.flag_code = flag_code
        self.country_name = country_name
        self.pattern = pattern

    def get_cube_requests(self, target_zones: List[TargetZone]) -> List["CubeRequest"]:
        cube_requests = []
        target_zones = target_zones[::-1]
        for i in range(2, -1, -1):
            for j in range(2,-1,-1):
                colour = self.pattern[i][j]
                if not colour == CubeColour.NONE:
                    target_zone_position = target_zones[i * 3 + j].position
                    dropoff_position = WorldCoordinate(target_zone_position.x, target_zone_position.y + 0.22)
                    request = CubeRequest(colour, dropoff_position)
                    cube_requests.append(request)

        return cube_requests


class CubeRequest(object):
    """Get a block of this colour, and drop it there."""

    def __init__(self, block_colour: int, drop_location: WorldCoordinate):
        self.blockColour = block_colour
        self.drop_position = drop_location


class FlagRepository(object):

    def get_flag(self, flag_code: int):
        raise NotImplementedError


class HardcodedSingleFlagRepository(FlagRepository):

    def __init__(self, flag: Flag):
        self.flag = flag

    def get_flag(self, flag_code: int) -> Flag:
        return self.flag
