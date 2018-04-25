import threading

import time

from atlas.game.BoardFactory import BoardFactory


class GameStatusUpdater(object):
    def __init__(self, board_factory: BoardFactory):
        self.shouldStop = False
        self.board_factory = board_factory
        self.thread = threading.Thread(target=self.run)

    def run(self):
        while not self.shouldStop:
            time.sleep(1)
            try:
                self.board_factory.create_board()
            except Exception:
                continue

    def start(self):
        self.thread.start()

    def stop(self):
        self.shouldStop = True
