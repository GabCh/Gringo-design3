from atlas.game.ir_code_reader import IrCodeReader


class SimulatedIrCodeReader(IrCodeReader):

    def get_ir_code(self) -> int:
        return 34

    def is_receiving_stable_code(self) -> bool:
        return True
