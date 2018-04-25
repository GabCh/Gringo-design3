import os

from atlas.infrastructure.ServiceLocator import ServiceLocator
from atlas.infrastructure.yaml_config_loader import load_yaml_config, ApplicationProperties


class AbstractBinder(object):

    def bind(self, service_locator: ServiceLocator):
        raise NotImplementedError


class MissingYamlConfigFileException(Exception):
    pass


class AbstractContext(object):
    INSTANCE = None

    def __init__(self):
        self.serviceLocator = ServiceLocator()
        self.configure_service_locator()
        config_file = os.path.expanduser(self.yaml_config_filename())
        if not os.path.exists(config_file):
            raise MissingYamlConfigFileException(config_file)
        self.config = load_yaml_config(config_file)
        self.serviceLocator.bind(ApplicationProperties, self.config)
        AbstractContext.INSTANCE = self

    def configure_service_locator(self):
        raise NotImplementedError

    def service_locator(self) -> ServiceLocator:
        return self.serviceLocator

    def yaml_config_filename(self) -> str:
        raise NotImplementedError
