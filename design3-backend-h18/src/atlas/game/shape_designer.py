import numpy as np

from atlas.game.CubeStorage import CubeStorage
from atlas.game.board_elements import Obstacle


class ShapeDesigner(object):

    def __init__(self, canvas: np.array):
        self.canvas = canvas
        h, w = self.canvas.shape
        self.width = w
        self.height = h

    def generate_circle(self, obstacle: Obstacle, diameter: float) -> np.array:

        radius = int(diameter / 2)

        x = int(obstacle.position.x * 100)
        y = int(obstacle.position.y * 100)

        i_0 = x - radius
        j_0 = y - radius

        for i in range(i_0, int(i_0 + diameter + 1)):
            for j in range(j_0, int(j_0 + diameter + 1)):
                dx = abs(i - x)
                dy = abs(j - y)
                hypot = np.hypot(dx, dy)
                if hypot <= (diameter / 2) and i < self.height and j < self.width:
                    self.canvas[i, j] = 1

    def generate_borders(self, border: int):

        for i in range(self.height):
            for j in range(int(border)):
                self.canvas[i, j] = 1
                self.canvas[i, ((self.width - 1) - j)] = 1

        for j in range(self.width):
            for i in range(int(border)):
                self.canvas[i, j] = 1
                self.canvas[((self.height - 1) - i), j] = 1

    def generate_cube_storage(self, border: int, storage_lenght: int):
        for i in range(self.height):
            for j in range(border):
                self.canvas[i, ((self.width - 1) - j)] = 1

        for j in range(int(self.width - storage_lenght), self.width):
            for i in range(border):
                self.canvas[i, j] = 1
                self.canvas[((self.height - 1) - i), j] = 1

    def generate_cube(self, cube_storage: CubeStorage, width: int):

        cubes = cube_storage.cubes
        for cube in cubes:

            i_0 = int((cube.position.y * 100) - width/2)
            j_0 = int((cube.position.x * 100) - width/2)
            for i in range(i_0, i_0 + width):
                for j in range(j_0, j_0 + width):
                    if i < self.width and j < self.height:
                        self.canvas[j, i] = 1
