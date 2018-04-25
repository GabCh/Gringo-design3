from typing import List

from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.board import Board
from atlas.logging import LoggerFactory


class CreateFlagTask(Task):
    LOGGER = LoggerFactory.get_logger("CreateFlagTask")

    def __init__(self, board_factory: BoardFactory, task_scheduler: TaskScheduler, task_factory: "TaskFactory"):
        self.task_factory = task_factory
        self.board_factory = board_factory
        self.task_scheduler = task_scheduler

    def run(self):
        board = self.board_factory.create_board()

        if not board.objective_flag_container.is_flag_present():
            self.LOGGER.error("Flag not present. Aborting.")
            raise FlagNotPresentException()

        for task in self.get_fetch_block_tasks(board):
            self.task_scheduler.add_task(task)
        end_competition_task = self.task_factory.create_task("end_competition")
        self.task_scheduler.add_task(end_competition_task)

    def get_fetch_block_tasks(self, board: Board) -> List[Task]:
        tasks = []
        flag = board.objective_flag_container.get()
        for cube_request in flag.get_cube_requests(board.targetZones):
            tasks.append(self.task_factory.create_task("fetch",
                                                       **{"colour": cube_request.blockColour,
                                                          "x": cube_request.drop_position.x,
                                                          "y": cube_request.drop_position.y}))
        return tasks


class FlagNotPresentException(Exception):
    pass
