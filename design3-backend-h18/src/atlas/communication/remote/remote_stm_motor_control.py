from atlas.communication.remote.remote_robot_communication import RemoteRobotCommunication
from atlas.motor.motor_control import MotorControl


class RemoteStmMotorControl(MotorControl):

    def __init__(self, robot_communication: RemoteRobotCommunication):
        self.robot_communication = robot_communication

    def rotate(self, angle: int):
        self.robot_communication.doRequest("POST", "/motor/rotate", {"angle": angle})

    def move_forward(self, distance: float):
        self.robot_communication.doRequest("POST", "/motor/forward", {"distance": distance})

    def move_left(self, distance: float):
        self.robot_communication.doRequest("POST", "/motor/left", {"distance": distance})

    def move_diagonal(self, forward: float, left: float):
        self.robot_communication.doRequest("POST", "/motor/diagonal", {"forward": forward, "left": left})
