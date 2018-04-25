import unittest

from atlas.game.Task import Task
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.game_status import GameStatus
from atlas.infrastructure.binder import AbstractContext
from atlasTesting.dummy_context import DummyContext


class TaskSchedulerTest(unittest.TestCase):
    SOME_TASK = Task()

    def setUp(self):
        self.taskScheduler = TaskScheduler()
        AbstractContext.INSTANCE = DummyContext()
        AbstractContext.INSTANCE.serviceLocator.bind(GameStatus, GameStatus())

    def test_whenCreatingTaskScheduler_thenQueueIsInitiallyEmpty(self):
        is_empty = self.taskScheduler.is_queue_empty()

        self.assertTrue(is_empty)

    def test_whenAddingTask_thenTaskIsAddedToTheQueue(self):
        self.taskScheduler.add_task(self.SOME_TASK)

        self.assertFalse(self.taskScheduler.is_queue_empty())
