from atlas.game.Task import Task
from atlas.logging import LoggerFactory
from atlas.motor.motor_control import MotorControl


class MoveLeftTask(Task):
    LOGGER = LoggerFactory.get_logger("MoveLeftTask")

    def __init__(self, motor_control: MotorControl, distance: float):
        self.distance = distance
        self.motor_control = motor_control

    def run(self):
        self.LOGGER.info("Moving left {}m.".format(self.distance))
        self.motor_control.move_left(self.distance)
