from atlas.game.tasks.Task import HelloTask, Task
from atlas.logging import LoggerFactory
from atlas.logging.Logger import Logger
from atlas.infrastructure import ServiceLocator

locator = ServiceLocator()
locator.bind(Task, HelloTask)
locator.bind(int, 5)
locator.bind(Logger, lambda: LoggerFactory.get_logger("foo"))

task = locator.get(Task)

print(task)
