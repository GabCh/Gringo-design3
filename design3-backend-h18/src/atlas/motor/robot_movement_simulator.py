import math

import numpy as np

from atlas.game.element_detectors import RobotLocator
from atlas.motor.motor_control import MotorControl
from atlas.vision.coordinates import CoordinateTranslator
from atlas.vision.image import Image
from atlas.vision.util import WorldCoordinate, OrientedPixelCoordinate


class RobotMovementSimulator(MotorControl, RobotLocator):

    def __init__(self, coordinate_translator: CoordinateTranslator):
        self.coordinate_translator = coordinate_translator
        self.angle = 0
        self.x = 0.0
        self.y = 0.0
        self.mu, self.sigma = 0, 0.0125  # Bornes aléatoires (changer au gout)

    def rotate(self, angle: int):
        s = self.make_some_noise()
        self.angle += (angle + s)

    def locate_robot(self, image: Image) -> OrientedPixelCoordinate:
        s = self.make_some_noise()
        current_coordinate = WorldCoordinate(self.x + s, self.y + s)
        return OrientedPixelCoordinate(self.coordinate_translator.world_to_pixel(current_coordinate), self.angle)

    def move_forward(self, distance: float):
        s = self.make_some_noise()
        distance += s
        radian_angle = self.angle * math.pi / 180
        self.x += distance * math.cos(radian_angle)
        self.y += distance * math.sin(radian_angle)

    def move_left(self, distance: float):
        s = self.make_some_noise()
        distance += s
        radian_angle = self.angle * math.pi / 180
        self.x += distance * math.sin(radian_angle)
        self.y += distance * math.cos(radian_angle)

    def make_some_noise(self):
        return np.random.normal(self.mu, self.sigma, 1)[0]
