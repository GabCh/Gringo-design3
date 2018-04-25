import time

from atlas.game.Task import Task
from atlas.game.cube_grab_control import CubeGrabControl
from atlas.logging import LoggerFactory


class GrabBlockTask(Task):
    LOGGER = LoggerFactory.get_logger("GrabBlockTask")

    def __init__(self, cube_grab_control: CubeGrabControl):
        self.cube_grab_control = cube_grab_control

    def run(self):
        self.LOGGER.info("raising block.")
        self.cube_grab_control.grab()
        time.sleep(2)
