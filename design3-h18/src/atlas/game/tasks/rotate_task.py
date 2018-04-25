from atlas.game.Task import Task
from atlas.logging import LoggerFactory
from atlas.motor.motor_control import MotorControl


class RotateTask(Task):
    LOGGER = LoggerFactory.get_logger("RotateTask")

    def __init__(self, motor_control: MotorControl, angle: int):
        self.motor_control = motor_control
        self.angle = angle

    def run(self):
        self.LOGGER.info("Rotating by {} degrees...".format(self.angle))
        self.motor_control.rotate(self.angle)
