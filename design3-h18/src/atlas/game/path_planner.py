from typing import List

from atlas.game.board import Board
from atlas.vision.util import WorldCoordinate


class PathPlanner(object):

    def plan(self, start: WorldCoordinate, goal: WorldCoordinate, board: Board) -> List[WorldCoordinate]:
        raise NotImplementedError
