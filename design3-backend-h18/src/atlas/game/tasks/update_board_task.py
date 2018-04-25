from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task


class UpdateBoardTask(Task):

    def __init__(self, board_factory: BoardFactory):
        self.boardFactory = board_factory

    def run(self):
        self.boardFactory.create_board()
