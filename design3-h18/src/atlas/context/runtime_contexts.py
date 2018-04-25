from atlas.context.binder_config import CommonBinder, LocalVisionBinder, ConsoleLoggingBinder, \
    SimulatedRobotMovementBinder, StmRobotMotorControlBinder, RemoteLoggingBinder, RemoteVisionBinder, \
    RemoteRobotMotorControlBinder
from atlas.infrastructure.binder import AbstractContext
from atlas.infrastructure.context import ApplicationContext


@ApplicationContext
class LocalDebugContext(AbstractContext):

    def configure_service_locator(self):
        CommonBinder().bind(self.serviceLocator)
        LocalVisionBinder().bind(self.serviceLocator)
        ConsoleLoggingBinder().bind(self.serviceLocator)
        SimulatedRobotMovementBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"


@ApplicationContext
class DebugFlaskLoggingContext(AbstractContext):

    def configure_service_locator(self):
        CommonBinder().bind(self.serviceLocator)
        RemoteVisionBinder().bind(self.serviceLocator)
        RemoteLoggingBinder().bind(self.serviceLocator)
        SimulatedRobotMovementBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"


@ApplicationContext
class RealStmNoVisionContext(AbstractContext):

    def configure_service_locator(self):
        CommonBinder().bind(self.serviceLocator)
        LocalVisionBinder().bind(self.serviceLocator)
        ConsoleLoggingBinder().bind(self.serviceLocator)
        StmRobotMotorControlBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"


@ApplicationContext
class RealStmRealVisionContext(AbstractContext):
    def configure_service_locator(self):
        CommonBinder().bind(self.serviceLocator)
        RemoteVisionBinder().bind(self.serviceLocator)
        RemoteLoggingBinder().bind(self.serviceLocator)
        StmRobotMotorControlBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"


@ApplicationContext
class QuicksilverContext(AbstractContext):
    def configure_service_locator(self):
        CommonBinder().bind(self.service_locator())
        RemoteVisionBinder().bind(self.serviceLocator)
        RemoteLoggingBinder().bind(self.serviceLocator)
        RemoteRobotMotorControlBinder().bind(self.serviceLocator)

    def yaml_config_filename(self) -> str:
        return "~/.atlas/debug.yml"
