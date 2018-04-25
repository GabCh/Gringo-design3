import time

from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.game_status_updater import GameStatusUpdater
from atlas.logging.Journal import JournalMessageConsumer
from atlas.server.server import FlaskServer


class ApplicationRunner(object):
    def __init__(self, journal_consumer: JournalMessageConsumer, task_scheduler: TaskScheduler,
                 flask_server: FlaskServer, game_status_updater:GameStatusUpdater):
        self.gameStatusUpdater = game_status_updater
        self.flask_server = flask_server
        self.journalConsumer = journal_consumer
        self.task_scheduler = task_scheduler
        self.shouldStop = False

    def run(self):
        self.task_scheduler.start()
        self.journalConsumer.start()
        self.flask_server.start()
        self.gameStatusUpdater.start()

        while not self.shouldStop:
            time.sleep(1)

        self.task_scheduler.stop_and_join()
        self.journalConsumer.stop()

    def stop(self):
        self.shouldStop = True
