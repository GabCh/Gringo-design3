from queue import Queue, Empty
from threading import Thread
from typing import List
from flask_socketio import SocketIO
import time


class Journal(object):

    def __init__(self, message_queue: Queue):
        self.messageQueue = message_queue

    def get_messages(self) -> List[str]:
        messages = []
        try:
            while not self.messageQueue.empty():
                messages.append(self.messageQueue.get_nowait())
        except Empty:
            pass
        return messages


class JournalMessageConsumer(object):
    def __init__(self, journal: Journal, *, refresh_rate=0.5):
        self.journal = journal
        self.refreshRate = refresh_rate
        self.shouldStop = False
        self.runner = Thread(target=self._run)

    def start(self):
        self.runner.start()

    def _run(self):
        while not self.shouldStop:
            self._consume_messages()

    def stop(self):
        self.shouldStop = True
        self._consume_messages()

    def _consume_messages(self):
        raise NotImplementedError


class ConsoleOutputJournalMessageConsumer(JournalMessageConsumer):

    def _consume_messages(self):
        for message in self.journal.get_messages():
            print(message)
        time.sleep(self.refreshRate)


class RemoteOutputJournalMessageConsumer(JournalMessageConsumer):
    def __init__(self, socket_io: SocketIO, journal: Journal):
        super().__init__(journal)
        self.socket_io = socket_io

    def _consume_messages(self):
        for message in self.journal.get_messages():
            print(message)
            self.socket_io.emit('logging', message)
        time.sleep(self.refreshRate)
