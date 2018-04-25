from atlas.game.TaskFactory import TaskFactory
from atlas.game.TaskScheduler import TaskScheduler
from atlas.logging import LoggerFactory
from atlas.logging.Journal import ConsoleOutputJournalMessageConsumer

taskScheduler = TaskScheduler()
taskFactory = TaskFactory()
helloTask = taskFactory.create_task("hello_task", times=5, interval=1)
taskScheduler.add_task(helloTask)
journal = LoggerFactory.get_journal()
journal_consumer = ConsoleOutputJournalMessageConsumer(journal)

journal_consumer.start()
taskScheduler.start()

taskScheduler.stop_and_join()
journal_consumer.stop()
