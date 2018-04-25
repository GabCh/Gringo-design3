import math

from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task
from atlas.motor.motor_control import MotorControl
from atlas.vision.util import WorldCoordinate


class RealignTask(Task):

    def __init__(self, motor_control: MotorControl, board_factory: BoardFactory, destination: WorldCoordinate):
        self.destination = destination
        self.board_factory = board_factory
        self.motor_control = motor_control

    def run(self):
        board = self.board_factory.create_board()
        current_position = board.robot.position
        distance = self.destination - current_position

        angle = distance.angle_radians() - math.radians(board.robot.angle)
        self.motor_control.move_diagonal(distance.length() * math.cos(angle), distance.length() * math.sin(angle))
