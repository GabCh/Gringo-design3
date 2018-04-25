import unittest
from queue import Queue

from atlas.logging.Journal import Journal


class JournalTest(unittest.TestCase):
    SOME_LOG_MESSAGE = "This is a message."

    def setUp(self):
        self.messageQueue = Queue()
        self.journal = Journal(self.messageQueue)

    def test_givenEmptyQueue_whenGettingMessages_thenNoMessagesAreReturned(self):
        messages = self.journal.get_messages()

        self.assertTrue(len(messages) == 0)

    def test_givenLoggedMessages_whenGettingMessages_thenAllMessagesAreReturned(self):
        self.messageQueue.put(self.SOME_LOG_MESSAGE)

        messages = self.journal.get_messages()

        self.assertEqual(1, len(messages))
        self.assertTrue(self.SOME_LOG_MESSAGE in messages[0])
