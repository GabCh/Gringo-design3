import serial

from atlas.infrastructure.binder import AbstractContext
from atlas.infrastructure.yaml_config_loader import ApplicationProperties
from atlas.logging import LoggerFactory


class Arduino(object):
    LOGGER = LoggerFactory.get_logger("Arduino")

    def __init__(self, application_properties: ApplicationProperties):
        self.ser = serial.Serial(application_properties['arduino']['port'], 9600, timeout=0)

    def get_ir(self) -> str:
        last_results = []
        while True:
            try:
                flagcode = self.ser.readline().decode('utf-8')
                print("got {}".format(flagcode))
            except self.ser.SerialTimeoutException:
                self.LOGGER.error('Data could not be read')
            last_results.append(flagcode)
            if last_results.count(flagcode) >= 1 and flagcode != "":
                self.LOGGER.info(flagcode)
                break
        return flagcode


arduino_instance = None


def get_arduino_singleton() -> Arduino:
    global arduino_instance
    if arduino_instance is None:
        properties = AbstractContext.INSTANCE.service_locator().get(ApplicationProperties)
        arduino_instance = Arduino(properties)
    return arduino_instance
