from atlas.game.Task import Task
from atlas.game.flag import FlagRepository
from atlas.game.game_status import GameStatus
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.logging import LoggerFactory


class SetFlagTask(Task):
    LOGGER = LoggerFactory.get_logger("SetFlagTask")

    def __init__(self, flag_repository: FlagRepository, flag_container: ObjectiveFlagContainer, game_status: GameStatus,
                 flag_code_to_set: int):
        self.game_status = game_status
        self.flag_code_to_set = flag_code_to_set
        self.flag_container = flag_container
        self.flag_repository = flag_repository

    def run(self):
        self.LOGGER.info("Setting flag to {}".format(self.flag_code_to_set))
        flag = self.flag_repository.get_flag(self.flag_code_to_set)
        self.flag_container.set(flag)
        self._update_game_status()

    def _update_game_status(self):
        if 'flag' not in self.game_status:
            self.game_status['flag'] = {}
        self.game_status['flag']['visual'] = self.flag_container.get().pattern
        self.game_status['flag']['name'] = self.flag_container.get().country_name
        self.game_status['flag']['number'] = self.flag_container.get().flag_code
