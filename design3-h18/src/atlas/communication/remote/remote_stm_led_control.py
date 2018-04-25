from atlas.communication.remote.remote_robot_communication import RemoteRobotCommunication
from atlas.game.led_control import LedControl


class RemoteStmLedControl(LedControl):
    def __init__(self, communication: RemoteRobotCommunication):
        self.communication = communication

    def turn_on(self):
        self.communication.doRequest('POST', "/led/on")

    def turn_off(self):
        self.communication.doRequest('POST', "/led/off")
