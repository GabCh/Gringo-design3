import json
from datetime import datetime
from typing import List

from atlas.game.initial_game_status import STARTING_SCHEMA
from atlas.vision.util import PixelCoordinate


class GameStatus(object):

    def __init__(self):
        self.content = STARTING_SCHEMA

    def __setitem__(self, key, value):
        self.content[key] = value

    def __getitem__(self, item):
        return self.content[item]

    def __contains__(self, item):
        return self.content.__contains__(item)

    def to_json(self) -> str:
        return json.dumps(self.content)

    def set_next_colour(self, block_colour: int):
        self.content['nextColour'] = block_colour

    def update_robot_actual_position_in_path(self, position: PixelCoordinate):
        self.content['vision']['path']['actual'].append({"x": position.x, "y": position.y})

    def set_new_path(self, path: List[PixelCoordinate]):
        format_coordinate = lambda coordinate: {"x": coordinate.x, "y": coordinate.y}

        self.content['vision']['path']['oldPlans'].append(self.content['vision']['path']['currentPlan'])
        self.content['vision']['path']['currentPlan'] = [format_coordinate(x) for x in path]
        self.content['vision']['path']['actual'] = []

    def start_timer(self):
        self.content['time']['start'] = self._current_time_millis()

    def stop_timer(self):
        self.content['time']['stop'] = self._current_time_millis()

    def _current_time_millis(self):
        epoch = datetime.utcfromtimestamp(0)
        start_time_millis = (datetime.utcnow() - epoch).total_seconds() * 1000.0
        return start_time_millis
