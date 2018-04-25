from atlas.game.Task import Task
from atlas.game.led_control import LedControl
from atlas.logging import LoggerFactory


class TurnOnLedTask(Task):
    LOGGER = LoggerFactory.get_logger('TurnOnLedTask')

    def __init__(self, led_control: LedControl):
        self.led_control = led_control

    def run(self):
        self.LOGGER.info("Turning on LED.")
        self.led_control.turn_on()
