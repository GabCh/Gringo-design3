from atlas.infrastructure.binder import AbstractContext


class DummyContext(AbstractContext):

    def configure_service_locator(self):
        pass

    def yaml_config_filename(self) -> str:
        return "/dev/null"
