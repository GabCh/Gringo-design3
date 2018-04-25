from atlas.game.Task import Task
from atlas.logging.Logger import Logger


class HelloTask(Task):
    """Logs hello a certain amount of times, at a given interval in seconds."""

    def __init__(self, logger: Logger, times: int, interval: int):
        self.logger = logger
        self.times = times
        self.interval = interval

    def run(self):
        for i in range(0, self.times):
            self.logger.info("hello")
            import time
            time.sleep(self.interval)
