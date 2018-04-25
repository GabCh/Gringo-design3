from atlas.communication.remote.remote_robot_communication import RemoteRobotCommunication
from atlas.game.cube_grab_control import CubeGrabControl


class RemoteCubeGrabControl(CubeGrabControl):

    def __init__(self, robot_communication: RemoteRobotCommunication):
        self.robot_communication = robot_communication

    def grab(self):
        self.robot_communication.doRequest("POST", "/grab")

    def release(self):
        self.robot_communication.doRequest("POST", "/release")
