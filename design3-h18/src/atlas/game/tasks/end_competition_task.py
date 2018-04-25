from atlas.game.Task import Task
from atlas.game.game_status import GameStatus


class EndCompetitionTask(Task):
    def __init__(self, game_status: GameStatus, task_factory: "TaskFactory"):
        self.task_factory = task_factory
        self.game_status = game_status

    def run(self):
        self.task_factory.create_task("goto", **{"x": 0.5, "y": 1.22, "angle": 0}).run()

        self.task_factory.create_task("led_on").run()
        self.game_status.stop_timer()
