from atlas.game.BoardFactory import BoardFactory
from atlas.game.Task import Task
from atlas.game.TaskScheduler import TaskScheduler
from atlas.game.cube_grab_control import CubeGrabControl
from atlas.game.flag import FlagRepository, CubeRequest
from atlas.game.game_status import GameStatus
from atlas.game.led_control import LedControl
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.game.path_planner import PathPlanner
from atlas.game.tasks.competition_task import CompetitionTask
from atlas.game.tasks.create_flag_task import CreateFlagTask
from atlas.game.tasks.end_competition_task import EndCompetitionTask
from atlas.game.tasks.fetch_block_task import FetchBlockTask
from atlas.game.tasks.get_ir_flag_code_task import GetIrFlagCodeTask
from atlas.game.tasks.goto_task import GoToTask
from atlas.game.tasks.grab_block_task import GrabBlockTask
from atlas.game.tasks.hello_task import HelloTask
from atlas.game.ir_code_reader import IrCodeReader
from atlas.game.tasks.move_forward_task import MoveForwardTask
from atlas.game.tasks.move_left_task import MoveLeftTask
from atlas.game.tasks.orient_to_task import OrientToTask
from atlas.game.tasks.realign_task import RealignTask
from atlas.game.tasks.release_block_task import ReleaseBlockTask
from atlas.game.tasks.rotate_task import RotateTask
from atlas.game.tasks.set_flag_task import SetFlagTask
from atlas.game.tasks.turn_off_led_task import TurnOffLedTask
from atlas.game.tasks.turn_on_led_task import TurnOnLedTask
from atlas.game.tasks.update_board_task import UpdateBoardTask
from atlas.infrastructure.binder import AbstractContext
from atlas.logging import LoggerFactory
from atlas.motor.motor_control import MotorControl
from atlas.vision.coordinates import CoordinateTranslator
from atlas.vision.util import WorldCoordinate, OrientedWorldCoordinate


class TaskFactory(object):

    def create_task(self, task_name: str, **kwargs) -> Task:
        service_locator = AbstractContext.INSTANCE.service_locator()

        if task_name == "hello_task":
            return HelloTask(LoggerFactory.get_logger("HelloTask"), **kwargs)
        if task_name == "update_board":
            return UpdateBoardTask(service_locator.get(BoardFactory))
        if task_name == "move_forward":
            return MoveForwardTask(service_locator.get(MotorControl), **kwargs)
        if task_name == "rotate":
            return RotateTask(service_locator.get(MotorControl), **kwargs)
        if task_name == "goto":
            return GoToTask(service_locator.get(PathPlanner), service_locator.get(BoardFactory),
                            service_locator.get(GameStatus), service_locator.get(CoordinateTranslator), self,
                            OrientedWorldCoordinate(WorldCoordinate(kwargs['x'], kwargs['y']), kwargs['angle']))
        if task_name == "set_flag":
            return SetFlagTask(service_locator.get(FlagRepository), service_locator.get(ObjectiveFlagContainer),
                               service_locator.get(GameStatus),
                               flag_code_to_set=kwargs['flag_code'])
        if task_name == "get_ir":
            return GetIrFlagCodeTask(service_locator.get(IrCodeReader), self)

        if task_name == "grab":
            return GrabBlockTask(service_locator.get(CubeGrabControl))

        if task_name == "release":
            return ReleaseBlockTask(service_locator.get(CubeGrabControl))

        if task_name == "orient_to":
            return OrientToTask(service_locator.get(MotorControl), service_locator.get(BoardFactory), **kwargs)

        if task_name == 'fetch':
            return FetchBlockTask(service_locator.get(BoardFactory), service_locator.get(GameStatus), self,
                                  CubeRequest(kwargs['colour'], WorldCoordinate(kwargs['x'], kwargs['y'])))
        if task_name == "move_left":
            return MoveLeftTask(service_locator.get(MotorControl), kwargs['distance'])

        if task_name == "realign":
            return RealignTask(service_locator.get(MotorControl), service_locator.get(BoardFactory),
                               WorldCoordinate(kwargs['x'], kwargs['y']))
        if task_name == "start_competition":
            return CompetitionTask(service_locator.get(TaskScheduler), self, service_locator.get(BoardFactory),
                                   service_locator.get(GameStatus))
        if task_name == "create_flag":
            return CreateFlagTask(service_locator.get(BoardFactory), service_locator.get(TaskScheduler), self)

        if task_name == "led_on":
            return TurnOnLedTask(service_locator.get(LedControl))
        if task_name == "led_off":
            return TurnOffLedTask(service_locator.get(LedControl))
        if task_name == "end_competition":
            return EndCompetitionTask(service_locator.get(GameStatus), self)
