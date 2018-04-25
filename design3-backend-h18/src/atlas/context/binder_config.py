from atlas.communication.arduino import Arduino, get_arduino_singleton
from atlas.communication.arduino_ir_reader import ArduinoIrReader
from atlas.communication.remote.remote_cube_grab_control import RemoteCubeGrabControl
from atlas.communication.remote.remote_ir_reader import RemoteIrReader
from atlas.communication.remote.remote_robot_communication import RemoteRobotCommunication
from atlas.communication.remote.remote_stm_led_control import RemoteStmLedControl
from atlas.communication.remote.remote_stm_motor_control import RemoteStmMotorControl
from atlas.communication.sercom_ident import StmUsbCtl
from atlas.communication.stm_cube_grab_control import StmCubeGrabControl
from atlas.communication.stm_led_control import StmLedControl
from atlas.communication.stm_motor_control import get_stm_usb_ctl_singleton, StmMotorControl
from atlas.game.BoardFactory import BoardFactory, VisionBoardFactory
from atlas.game.ConverterFactory import get_calibrated_coordinate_translator
from atlas.game.TaskFactory import TaskFactory
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.competitionFlagRepository import CompetitionFlagRepository
from atlas.game.cube_grab_control import CubeGrabControl
from atlas.game.element_detectors import TargetZoneLocator, BlockLocator, ObstacleLocator, RobotLocator, TableLocator
from atlas.game.flag import FlagRepository
from atlas.game.game_status import GameStatus
from atlas.game.game_status_updater import GameStatusUpdater
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.game.path_planner import PathPlanner
from atlas.game.simulated.simulated_ir_code_reader import SimulatedIrCodeReader
from atlas.game.ir_code_reader import IrCodeReader
from atlas.game.led_control import LedControl
from atlas.infrastructure import ServiceLocator
from atlas.infrastructure.binder import AbstractBinder
from atlas.logging import LoggerFactory
from atlas.logging.Journal import JournalMessageConsumer, ConsoleOutputJournalMessageConsumer, \
    RemoteOutputJournalMessageConsumer
from atlas.motor.motor_control import MotorControl
from atlas.motor.robot_movement_simulator import RobotMovementSimulator
from atlas.pathfinder.highway_planner import HighwayPlanner
from atlas.pathfinder.orthogonal_projection_calculator import OrthogonalProjectionCalculator
from atlas.pathfinder.tree_walker import TreeWalker
from atlas.server.app import socket_io
from atlas.server.app.remote_web_image_repository import RemoteWebImageRepository
from atlas.server.server import FlaskServer
from atlas.vision.coordinates import CoordinateTranslator, DummyHardcodedCoordinateTranslator
from atlas.vision.image_repository import LocalDirectoryImageRepository, ImageRepository
from atlas.vision.util import PixelCoordinate
from atlas.vision.vision_element_detector import VisionBlockLocator, VisionObstacleLocator, VisionRobotLocator, \
    VisionTableLocator
from atlasTesting.single_image_repository import SingleImageRepository


class CommonBinder(AbstractBinder):
    """Bind dependencies which are common to all configurations."""

    def bind(self, service_locator: ServiceLocator):
        scheduler = TaskScheduler()
        task_factory = TaskFactory()
        image_repository = RemoteWebImageRepository()
        service_locator.bind(ImageRepository, image_repository)
        service_locator.bind(GameStatus, GameStatus())
        service_locator.bind(GameStatusUpdater, GameStatusUpdater)
        service_locator.bind(TaskScheduler, scheduler)
        service_locator.bind(TaskFactory, TaskFactory)
        service_locator.bind(ServiceLocator, service_locator)
        service_locator.bind(FlaskServer, FlaskServer(scheduler, task_factory, image_repository))
        service_locator.bind(ObjectiveFlagContainer, ObjectiveFlagContainer())
        service_locator.bind(TargetZoneLocator, HardcodedTargetZoneLocator)
        service_locator.bind(PathPlanner, HighwayPlanner)
        service_locator.bind(FlagRepository, CompetitionFlagRepository)
        service_locator.bind(OrthogonalProjectionCalculator, OrthogonalProjectionCalculator)
        service_locator.bind(TreeWalker, TreeWalker)


class LocalVisionBinder(AbstractBinder):
    DATASET_DIRECTORY = "../infra/training_datasets/blocks"

    def bind(self, service_locator: ServiceLocator):
        local_directory = LocalDirectoryImageRepository(self.DATASET_DIRECTORY)
        service_locator.bind(ImageRepository, SingleImageRepository(local_directory.get_next_image()))
        coordinate_translator = DummyHardcodedCoordinateTranslator()
        service_locator.bind(CoordinateTranslator, coordinate_translator)
        service_locator.bind(BoardFactory, VisionBoardFactory)
        service_locator.bind(RobotLocator, VisionRobotLocator)
        service_locator.bind(ObstacleLocator, VisionObstacleLocator)
        service_locator.bind(BlockLocator, VisionBlockLocator)


class RemoteVisionBinder(AbstractBinder):

    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(CoordinateTranslator, get_calibrated_coordinate_translator)
        service_locator.bind(TableLocator, VisionTableLocator)
        service_locator.bind(BoardFactory, VisionBoardFactory)
        service_locator.bind(RobotLocator, VisionRobotLocator)
        service_locator.bind(ObstacleLocator, VisionObstacleLocator)
        service_locator.bind(BlockLocator, VisionBlockLocator)


class ConsoleLoggingBinder(AbstractBinder):

    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(JournalMessageConsumer, ConsoleOutputJournalMessageConsumer(LoggerFactory.get_journal()))


class SimulatedRobotMovementBinder(AbstractBinder):
    def bind(self, service_locator: ServiceLocator):
        coordinate_translator = CoordinateTranslator(1280, 3.23, PixelCoordinate(343, 363))
        simulator = RobotMovementSimulator(coordinate_translator)
        service_locator.bind(MotorControl, simulator)
        service_locator.bind(RobotLocator, simulator)
        service_locator.bind(IrCodeReader, SimulatedIrCodeReader)


class RemoteLoggingBinder(AbstractBinder):

    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(JournalMessageConsumer,
                             RemoteOutputJournalMessageConsumer(socket_io, LoggerFactory.get_journal()))


class StmRobotMotorControlBinder(AbstractBinder):
    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(StmUsbCtl, get_stm_usb_ctl_singleton)
        service_locator.bind(MotorControl, StmMotorControl)
        service_locator.bind(CubeGrabControl, StmCubeGrabControl)
        service_locator.bind(Arduino, get_arduino_singleton)
        service_locator.bind(IrCodeReader, ArduinoIrReader)
        service_locator.bind(LedControl, StmLedControl)


class RemoteRobotMotorControlBinder(AbstractBinder):
    def bind(self, service_locator: ServiceLocator):
        service_locator.bind(RemoteRobotCommunication, RemoteRobotCommunication)
        service_locator.bind(MotorControl, RemoteStmMotorControl)
        service_locator.bind(CubeGrabControl, RemoteCubeGrabControl)
        service_locator.bind(IrCodeReader, RemoteIrReader)
        service_locator.bind(LedControl, RemoteStmLedControl)
