import datetime

from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.game_status import GameStatus


class CompetitionTask(Task):

    def __init__(self, task_scheduler: TaskScheduler, task_factory: "TaskFactory", board_factory: BoardFactory,
                 game_status: GameStatus):
        self.game_status = game_status
        self.board_factory = board_factory
        self.task_factory = task_factory
        self.task_scheduler = task_scheduler

    def run(self):
        board = self.board_factory.create_board()
        self.game_status.start_timer()

        if not board.objective_flag_container.is_flag_present():
            goto_read_ir = self.task_factory.create_task("goto", **{"x": 0.5, "y": 0.5, "angle": 43})
            get_ir_task = self.task_factory.create_task("get_ir")
            self.task_scheduler.add_task(goto_read_ir)
            self.task_scheduler.add_task(get_ir_task)

        self.task_scheduler.add_task(self.task_factory.create_task("create_flag"))
