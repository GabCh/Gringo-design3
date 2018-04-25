import time

from atlas.game.Task import Task
from atlas.game.cube_grab_control import CubeGrabControl


class ReleaseBlockTask(Task):

    def __init__(self, cube_grab_control: CubeGrabControl):
        self.cube_grab_control = cube_grab_control

    def run(self):
        self.cube_grab_control.release()
        time.sleep(2)
