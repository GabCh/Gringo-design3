from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task
from atlas.logging import LoggerFactory
from atlas.motor.motor_control import MotorControl


class OrientToTask(Task):
    LOGGER = LoggerFactory.get_logger("OrientToTask")

    def __init__(self, motor_control: MotorControl, board_factory: BoardFactory, angle: int):
        self.angle = angle
        self.board_factory = board_factory
        self.motor_control = motor_control

    def run(self):
        self.LOGGER.info("Orienting to {}".format(self.angle))
        current_robot_angle = self.board_factory.create_board().robot.angle
        self.LOGGER.debug("currently at angle {}".format(current_robot_angle))
        angle_distance = (self.angle - current_robot_angle) % 360
        self.LOGGER.debug("rotating by {}".format(angle_distance))
        self.motor_control.rotate(angle_distance)
