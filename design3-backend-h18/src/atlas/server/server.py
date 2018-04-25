import os
import threading

from atlas.game.TaskFactory import TaskFactory
from atlas.game.TaskScheduler import TaskScheduler
from atlas.logging import LoggerFactory
from atlas.server.app import create_app, socket_io
from atlas.server.app.remote_web_image_repository import RemoteWebImageRepository


class FlaskServer(object):
    LOGGER = LoggerFactory.get_logger("FlaskServer")

    def __init__(self, task_scheduler: TaskScheduler, task_factory: TaskFactory,
                 image_repository: RemoteWebImageRepository):
        self.configName = os.getenv('APP_SETTINGS') or 'testing'
        self.app = create_app(task_scheduler, task_factory, image_repository)
        self.runner = threading.Thread(target=self._run_app)

    def _run_app(self):
        import logging
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        socket_io.run(self.app, host='0.0.0.0', port=8080)

    def start(self):
        self.LOGGER.info("Starting FlaskServer...")
        self.runner.start()
