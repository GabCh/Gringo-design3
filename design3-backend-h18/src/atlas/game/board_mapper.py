import numpy as np

from atlas.game.obstacle_map import ObstacleMap
from atlas.game.shape_designer import ShapeDesigner


class BoardMapper(object):

    @staticmethod
    def generate(board: "Board", obstacle_diameter: int, cube_width: int, border_width: int,
                 cube_storage_lenght: int, cube_storage_width: int) -> ObstacleMap:

        barrier_pixels = np.zeros((board.height, board.width))
        shape_designer = ShapeDesigner(barrier_pixels)

        shape_designer.generate_borders(border_width)

        for obstacle in board.obstacles:
            shape_designer.generate_circle(obstacle, obstacle_diameter)

        shape_designer.generate_cube(board.cubeStorage, cube_width)
        shape_designer.generate_cube_storage(cube_storage_width, cube_storage_lenght)

        return ObstacleMap(barrier_pixels)
