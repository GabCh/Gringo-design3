from datetime import datetime
from queue import Queue

from atlas.logging.Journal import Journal
from atlas.logging.Logger import Logger, LogLevel

globalQueue = Queue()


def get_logger(classname: str) -> Logger:
    return NamedLogger(globalQueue, classname, _get_global_logging_level())


def get_journal() -> Journal:
    return Journal(globalQueue)


def _get_global_logging_level():
    # TODO return from some sort of context/config
    return LogLevel.DEBUG


class NamedLogger(Logger):
    def __init__(self, queue: Queue, name: str, log_level: int):
        self.queue = queue
        self.name = name
        self.logLevel = log_level

    def info(self, message: str):
        if self._should_log(LogLevel.INFO):
            self.queue.put(self._format_message(message, LogLevel.INFO))

    def warn(self, message: str):
        if self._should_log(LogLevel.WARNING):
            self.queue.put(self._format_message(message, LogLevel.WARNING))

    def debug(self, message: str):
        if self._should_log(LogLevel.DEBUG):
            self.queue.put(self._format_message(message, LogLevel.DEBUG))

    def error(self, message: str):
        if self._should_log(LogLevel.ERROR):
            self.queue.put(self._format_message(message, LogLevel.ERROR))

    def _format_message(self, message: str, log_level) -> str:
        return "{} - [{}] {} - {}".format(LogLevel.to_string(log_level), self.name, datetime.now(), message)

    def _should_log(self, log_level):
        return log_level >= self.logLevel
