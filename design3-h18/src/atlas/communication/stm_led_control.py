from atlas.communication.sercom_ident import StmUsbCtl
from atlas.game.led_control import LedControl


class StmLedControl(LedControl):
    def __init__(self, stm_control: StmUsbCtl):
        self.stmUsbControl = stm_control

    def turn_on(self):
        self.stmUsbControl.led_control(1)

    def turn_off(self):
        self.stmUsbControl.led_control(0)
