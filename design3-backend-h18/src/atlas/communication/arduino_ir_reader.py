from atlas.communication.arduino import Arduino
from atlas.game.ir_code_reader import IrCodeReader, CannotGetIrException


class ArduinoIrReader(IrCodeReader):

    def __init__(self, arduino: Arduino):
        self.arduino = arduino

    def get_ir_code(self) -> int:
        for counter in range(0, 3):
            code = self.arduino.get_ir()
            if code != "":
                return int(code)
        raise CannotGetIrException()
