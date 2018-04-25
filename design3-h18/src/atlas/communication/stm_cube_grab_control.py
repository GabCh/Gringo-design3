from atlas.communication.sercom_ident import StmUsbCtl
from atlas.game.cube_grab_control import CubeGrabControl


class StmCubeGrabControl(CubeGrabControl):
    def __init__(self, stm_usb_ctl: StmUsbCtl):
        self.stm_usb_ctl = stm_usb_ctl

    def grab(self):
        self.stm_usb_ctl.prehensor_ctl(lift=1)

    def release(self):
        self.stm_usb_ctl.prehensor_ctl(lift=0)
