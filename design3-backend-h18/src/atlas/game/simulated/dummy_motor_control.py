from atlas.game.cube_grab_control import CubeGrabControl
from atlas.motor.motor_control import MotorControl


class DummyMotorControl(MotorControl):
    def rotate(self, angle: int):
        pass

    def move_forward(self, distance: float):
        pass

    def move_left(self, distance: float):
        pass


class DummyCubeGrabControl(CubeGrabControl):
    def grab(self):
        pass

    def release(self):
        pass
