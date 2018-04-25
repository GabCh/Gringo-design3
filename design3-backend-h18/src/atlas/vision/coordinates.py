import numpy as np
import json
import os
from atlas.vision.util import PixelCoordinate, WorldCoordinate, OrientedPixelCoordinate, OrientedWorldCoordinate


class CoordinateTranslator(object):

    def __init__(self, pixel_width: int, world_width: float, origin: PixelCoordinate):
        self.origin = origin
        self.pixel_to_world_ratio = world_width / pixel_width  # meters per pixel

    def pixel_to_world(self, point: PixelCoordinate, height: int = 0) -> WorldCoordinate:
        return WorldCoordinate(point.y * self.pixel_to_world_ratio, point.x * self.pixel_to_world_ratio)

    def world_to_pixel(self, point: WorldCoordinate, height=25) -> PixelCoordinate:
        return PixelCoordinate(int(point.y / self.pixel_to_world_ratio), int(point.x / self.pixel_to_world_ratio))


class CalibratedCoordinateTranslator(CoordinateTranslator):

    def __init__(self):
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, 'calibration.json')
        with open(path) as calibration_data:
            data = json.load(calibration_data)
            self.intrinsic = np.array(data['intrinsic'])
            self.extrinsic = np.array(data['extrinsic'])
            self.coefs = np.array(data['coefs'])
            self.matrix = np.matmul(self.intrinsic, self.extrinsic)
        self.origin = self.world_to_pixel(WorldCoordinate(0, 0))

    def pixel_to_world(self, point: PixelCoordinate, height: int = 0) -> WorldCoordinate:
        numerator = (-self.matrix[0, 3] + point.x * self.matrix[2, 3]) * \
                    (self.matrix[1, 1] - point.y * self.matrix[2, 1]) - \
                    (self.matrix[1, 3] - point.y * self.matrix[2, 3]) * \
                    (-self.matrix[0, 1] + point.x * self.matrix[2, 1]) - \
                    height * ((self.matrix[0, 1] - point.x * self.matrix[2, 1]) *
                              (self.matrix[1, 2] - point.y * self.matrix[2, 2]) -
                              (self.matrix[0, 2] - point.x * self.matrix[2, 2]) *
                              (self.matrix[1, 1] - point.y * self.matrix[2, 1]))
        denominator = (self.matrix[0, 0] - point.x * self.matrix[2, 0]) * \
                      (self.matrix[1, 1] - point.y * self.matrix[2, 1]) + \
                      (self.matrix[0, 1] - point.x * self.matrix[2, 1]) * \
                      (-self.matrix[1, 0] + point.y * self.matrix[2, 0])
        x = numerator / denominator

        numerator = (-self.matrix[0, 3] + point.x * self.matrix[2, 3]) * \
                    (-self.matrix[1, 0] + point.y * self.matrix[2, 0]) - \
                    (self.matrix[1, 3] - point.y * self.matrix[2, 3]) * \
                    (self.matrix[0, 0] - point.x * self.matrix[2, 0]) - \
                    height * ((self.matrix[0, 2] - point.x * self.matrix[2, 2]) *
                              (self.matrix[1, 0] - point.y * self.matrix[2, 0]) -
                              (self.matrix[0, 0] - point.x * self.matrix[2, 0]) *
                              (self.matrix[1, 2] - point.y * self.matrix[2, 2]))
        denominator = (self.matrix[0, 0] - point.x * self.matrix[2, 0]) * \
                      (self.matrix[1, 1] - point.y * self.matrix[2, 1]) + \
                      (self.matrix[0, 1] - point.x * self.matrix[2, 1]) * \
                      (-self.matrix[1, 0] + point.y * self.matrix[2, 0])
        y = numerator / denominator
        x = x / 102
        y = y / 105
        return WorldCoordinate(y, x)

    def world_to_pixel(self, point: WorldCoordinate, height: int = 0) -> PixelCoordinate:
        centimeter_point = WorldCoordinate(point.y * 102, point.x * 105)
        m_1_transposed = np.transpose(self.matrix[0, :])
        m_2_transposed = np.transpose(self.matrix[1, :])
        m_3_transposed = np.transpose(self.matrix[2, :])
        world = _HomogeneousCoordinateTransform(_CartesianCoordinate(centimeter_point)).apply()
        u = (np.matmul(m_1_transposed, world.coordinate) / np.matmul(m_3_transposed, world.coordinate))
        v = (np.matmul(m_2_transposed, world.coordinate) / np.matmul(m_3_transposed, world.coordinate))

        return PixelCoordinate(int(u), int(v))

    def oriented_pixel_to_world(self, point: OrientedPixelCoordinate) -> OrientedWorldCoordinate:
        world = self.pixel_to_world(point.coordinate)
        return OrientedWorldCoordinate(world, point.angle)

    def oriented_world_to_pixel(self, point: OrientedWorldCoordinate) -> OrientedPixelCoordinate:
        pixel = self.world_to_pixel(point.coordinate)
        return OrientedPixelCoordinate(pixel, point.angle)


class DummyHardcodedCoordinateTranslator(CoordinateTranslator):
    def __init__(self):
        # super().__init__(1159, 2.32, PixelCoordinate(343, 363))
        super().__init__(1159, 2.32, PixelCoordinate(0, 0))


class _CartesianCoordinate:

    def __init__(self, point: WorldCoordinate, z=0):
        self.coordinate = np.array([point.x, point.y, z])


class _HomogeneousCoordinate:

    def __init__(self, x, y, z=0):
        self.coordinate = np.array([x, y, z, 1])


class _HomogeneousCoordinateTransform:

    def __init__(self, cartesian_coordinate: _CartesianCoordinate):
        self.cartesian_coordinate = cartesian_coordinate

    def apply(self) -> _HomogeneousCoordinate:
        coordinate = self.cartesian_coordinate.coordinate
        return _HomogeneousCoordinate(coordinate[0], coordinate[1], coordinate[2])
