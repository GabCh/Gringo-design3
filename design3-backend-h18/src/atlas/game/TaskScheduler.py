import threading
import time
from queue import Queue

from atlas.game.Task import Task
from atlas.game.game_status import GameStatus
from atlas.infrastructure.binder import AbstractContext
from atlas.logging import LoggerFactory


class TaskScheduler(object):
    LOGGER = LoggerFactory.get_logger("TaskScheduler")

    def __init__(self):
        self.taskQueue = Queue()
        self.runner = None
        self.shouldStop = False

    def add_task(self, task: Task):
        self.taskQueue.put(task)
        self._game_status_queue_task(task.__class__.__name__)

    def start(self):
        self.LOGGER.info("Task runner starting up...")
        self.runner = threading.Thread(target=self._run_tasks)
        self.runner.start()

    def is_queue_empty(self) -> bool:
        return self.taskQueue.empty()

    def _run_tasks(self):
        self._init_game_status()
        while not self.shouldStop:
            if self.taskQueue.qsize() > 0:
                task = self.taskQueue.get()
                self._game_status_start_task()
                try:
                    task.run()
                except Exception as e:
                    self.LOGGER.error("Uncaught exception in task {}".format(task.__class__.__name__))
                    self.LOGGER.error("{},{}".format(e.__class__, str(e)))
                finally:
                    self._game_status_complete_task()
            else:
                time.sleep(1)

    def stop_and_join(self):
        self.shouldStop = True
        if self.runner.is_alive:
            self.runner.join()
        self.LOGGER.info("Task runner successfully stopped.")

    def _game_status_queue_task(self, new_task: str):
        self._init_game_status()
        self.game_status['tasks']['queued'].append(new_task)

    def _game_status_start_task(self):
        if len(self.game_status['tasks']['queued']) > 0:
            self.game_status['tasks']['current'] = self.game_status['tasks']['queued'][0]
            self.game_status['tasks']['queued'] = self.game_status['tasks']['queued'][1::]
        else:
            self.game_status['tasks']['current'] = None

    def _game_status_complete_task(self):
        self.game_status['tasks']['completed'].append(self.game_status['tasks']['current'])
        self.game_status['tasks']['current'] = None

    def _init_game_status(self):
        if 'tasks' not in self.game_status:
            self.game_status['tasks'] = {}
            self.game_status['tasks']['current'] = None
            self.game_status['tasks']['queued'] = []
            self.game_status['tasks']['completed'] = []

    @property
    def game_status(self) -> GameStatus:
        return AbstractContext.INSTANCE.service_locator().get(GameStatus)
