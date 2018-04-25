from atlas.communication.arduino_ir_reader import CannotGetIrException
from atlas.game.Task import Task
from atlas.game.ir_code_reader import IrCodeReader
from atlas.logging import LoggerFactory


class GetIrFlagCodeTask(Task):
    LOGGER = LoggerFactory.get_logger("GetIrFlagCodeTask")

    def __init__(self, ir_code_reader: IrCodeReader, task_factory: "TaskFactory"):
        self.task_factory = task_factory
        self.ir_code_reader = ir_code_reader

    def run(self):
        for i in range(0, 10):
            try:
                flag_code_to_set = self.ir_code_reader.get_ir_code()
                self.task_factory.create_task("set_flag", **{"flag_code": flag_code_to_set}).run()
                return
            except CannotGetIrException:
                self.task_factory.create_task("rotate", **{"angle": 10}).run()
