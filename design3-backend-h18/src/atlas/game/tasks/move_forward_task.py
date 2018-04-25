from atlas.game.Task import Task
from atlas.logging import LoggerFactory
from atlas.motor.motor_control import MotorControl


class MoveForwardTask(Task):
    LOGGER = LoggerFactory.get_logger("MoveForwardTask")

    def __init__(self, motor_control: MotorControl, distance: float):
        self.distance = distance
        self.motor_control = motor_control

    def run(self):
        self.LOGGER.info("Moving {}m forward...".format(self.distance))
        self.motor_control.move_forward(self.distance)
