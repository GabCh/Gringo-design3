from math import pi, radians
from time import sleep

from atlas.communication.sercom_ident import StmUsbCtl
from atlas.infrastructure.binder import AbstractContext
from atlas.infrastructure.yaml_config_loader import ApplicationProperties
from atlas.motor.motor_control import MotorControl

stmUsbCtl = None
CONSTANT_SPEED_DUTY_CYCLE = 0.5
CONSTANT_ROTATIONAL_SPEED = 285.04
CONSTANT_DIAMETER = 6.86323246438540764 / 100
CONSTANT_ROBOT_RADIUS = 24.54 / 100
CONSTANT_COMPLETE_REVOLUTION = 6400
CONSTANT_CIRCUMFERENCE = CONSTANT_DIAMETER * pi


def get_stm_usb_ctl_singleton() -> StmUsbCtl:
    global stmUsbCtl
    if stmUsbCtl is None:
        properties = AbstractContext.INSTANCE.service_locator().get(ApplicationProperties)
        stmUsbCtl = StmUsbCtl(properties)
    return stmUsbCtl


class StmMotorControl(MotorControl):

    def __init__(self, stm_usb_ctl: StmUsbCtl):
        self.stmCtl = stm_usb_ctl

    def rotate(self, angle: int):
        if angle < 180:
            distance = CONSTANT_ROBOT_RADIUS * radians(angle)
        else:
            distance = CONSTANT_ROBOT_RADIUS * radians(angle - 360)
        distanceInMotorPosition = int((distance / CONSTANT_CIRCUMFERENCE) * CONSTANT_COMPLETE_REVOLUTION * 0.5)
        if angle > 100:
            distanceInMotorPosition *= 0.85
        elif angle > 50:
            distanceInMotorPosition *= 0.9
        elif angle > 25:
            distanceInMotorPosition *= 0.95

        self.stmCtl.motor_rotate(int(distanceInMotorPosition))
        if angle > 90:
            sleep(3)
        else:
            sleep(2)

    def move_forward(self, distance: float):
        distanceInMotorPosition = int((distance / CONSTANT_CIRCUMFERENCE) * CONSTANT_COMPLETE_REVOLUTION)

        self.stmCtl.set_ypos_synced(distanceInMotorPosition)
        sleep(self.get_sleep_time(distance))

    def get_sleep_time(self, distance):
        return max(1.5 / 0.25 * abs(distance), 1.5)

    def move_left(self, distance: float):
        distanceInMotorPosition = int((distance / CONSTANT_CIRCUMFERENCE) * CONSTANT_COMPLETE_REVOLUTION)

        self.stmCtl.set_xpos_synced(-distanceInMotorPosition)
        sleep(self.get_sleep_time(distance))

    def move_diagonal(self, forward: float, left: float):
        distance_forward = int((forward / CONSTANT_CIRCUMFERENCE) * CONSTANT_COMPLETE_REVOLUTION)
        distance_left = int((left / CONSTANT_CIRCUMFERENCE) * CONSTANT_COMPLETE_REVOLUTION)
        self.stmCtl.set_ypos_synced(distance_forward)
        self.stmCtl.set_xpos_synced(-distance_left)
        sleep(max(self.get_sleep_time(forward), self.get_sleep_time(left)))
