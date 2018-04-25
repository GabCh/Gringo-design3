from typing import List

import numpy as np

from atlas.vision.util import WorldCoordinate


class ObstacleMap(object):

    def __init__(self, binary_matrix: np.array):
        self.matrix = binary_matrix

    def is_obstacle(self, x: int, y: int) -> bool:
        return self.matrix[x][y] != 0

    def get_neighbours(self, x: int, y: int) -> List[tuple]:
        potential_neighbours = []
        if x > 0:
            potential_neighbours.append((x - 1, y))
        if y > 0:
            potential_neighbours.append((x, y - 1))
        if x < self.height - 1:
            potential_neighbours.append((x + 1, y))
        if y < self.width - 1:
            potential_neighbours.append((x, y + 1))

        return [x for x in filter(lambda n: not self.is_obstacle(*n), potential_neighbours)]

    @property
    def width(self) -> int:
        return self.matrix.shape[1]

    @property
    def height(self) -> int:
        return self.matrix.shape[0]

    def get_tile_for_world_coordinate(self, coordinate: WorldCoordinate) -> tuple:
        x = int(coordinate.x * 100)
        y = int(coordinate.y * 100)
        return x, y

    def get_world_coordinate_for_tile(self, x: int, y: int) -> WorldCoordinate:
        return WorldCoordinate(x / 100.0, y / 100.0)
