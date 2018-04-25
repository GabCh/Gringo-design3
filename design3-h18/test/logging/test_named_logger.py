import unittest
from queue import Queue

from atlas.logging.Logger import LogLevel
from atlas.logging.LoggerFactory import NamedLogger


class NamedLoggerTest(unittest.TestCase):
    A_MESSAGE = "This is a message."

    def setUp(self):
        self.messageQueue = Queue()
        self.logger = NamedLogger(self.messageQueue, "test", LogLevel.DEBUG)

    def test_whenLogging_thenMessageIsAddedToQueue(self):
        self.logger.error(self.A_MESSAGE)

        self.assertEqual(1, self.messageQueue.qsize())

    def test_givenDebugLogLevel_whenLogging_thenShouldLogEverything(self):
        self.logger.debug(self.A_MESSAGE)
        self.logger.info(self.A_MESSAGE)
        self.logger.warn(self.A_MESSAGE)
        self.logger.error(self.A_MESSAGE)

        self.assertEqual(4, self.messageQueue.qsize())

    def test_givenErrorLogLevel_whenLogging_thenShouldOnlyLogErrors(self):
        error_logger = NamedLogger(self.messageQueue, "test", LogLevel.ERROR)

        error_logger.debug(self.A_MESSAGE)
        error_logger.info(self.A_MESSAGE)
        error_logger.warn(self.A_MESSAGE)
        error_logger.error(self.A_MESSAGE)

        self.assertEqual(1, self.messageQueue.qsize())
        message = self.messageQueue.get()
        self.assertTrue(self.A_MESSAGE in message and "ERROR" in message)


if __name__ == "__main__":
    unittest.main()
