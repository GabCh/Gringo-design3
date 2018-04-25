from typing import List

from atlas.communication.arduino_ir_reader import CannotGetIrException
from atlas.communication.remote.remote_robot_communication import RemoteRobotCommunication
from atlas.game.ir_code_reader import IrCodeReader
from atlas.logging import LoggerFactory


class RemoteIrReader(IrCodeReader):
    LOGGER = LoggerFactory.get_logger("RemoteIrReader")

    def __init__(self, robot_communication: RemoteRobotCommunication):
        self.robot_communication = robot_communication

    def get_ir_code(self) -> int:
        try:
            response = self.robot_communication.doRequest("GET", "/ir")
            return response.json()['ir']

        except Exception as e:
            self.LOGGER.error("Cannot get IR, {}".format(e))
            raise CannotGetIrException()

    def _majority_vote(self, codes: List[int]) -> int:
        elements = {}
        for code in codes:
            if code not in elements:
                elements[code] = 0
            elements[code] += 1

        most_frequent_code = None
        most_frequent_code_count = 0
        for code in elements.keys():
            if most_frequent_code is None:
                most_frequent_code = code
                most_frequent_code_count = elements[code]
            elif elements[code] > most_frequent_code_count:
                most_frequent_code = code
                most_frequent_code_count = elements[code]
        return most_frequent_code
