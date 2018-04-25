from typing import Optional

from atlas.game.flag import Flag


class ObjectiveFlagContainer(object):
    def __init__(self):
        self.flag = None

    def is_flag_present(self) -> bool:
        return self.flag is not None

    def get(self) -> Optional[Flag]:
        return self.flag

    def set(self, flag: Flag):
        self.flag = flag
