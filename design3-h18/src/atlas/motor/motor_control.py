class MotorControl(object):

    def rotate(self, angle: int):
        raise NotImplementedError

    def move_forward(self, distance: float):
        raise NotImplementedError

    def move_left(self, distance: float):
        raise NotImplementedError

    def move_diagonal(self, forward: float, left: float):
        raise NotImplementedError
