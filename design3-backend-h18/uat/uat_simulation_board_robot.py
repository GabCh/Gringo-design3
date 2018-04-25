from atlas.game import directions
from atlas.game.game_status import GameStatus
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.game.tasks.goto_task import GoToTask
from atlas.logging import LoggerFactory
from atlas.logging.Journal import ConsoleOutputJournalMessageConsumer
from atlas.motor.robot_movement_simulator import RobotMovementSimulator
from atlas.pathfinder.pathplanner import AStarPathPlanner
from atlas.vision.coordinates import DummyHardcodedCoordinateTranslator, CalibratedCoordinateTranslator
from atlas.vision.gameboard_visualizer import board_to_image
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.util import OrientedWorldCoordinate
from atlas.vision.vision_element_detector import VisionBlockLocator, VisionObstacleLocator, VisionTableLocator
from atlasTesting.feedback_giving_board_factory import FeedbackGivingBoardFactory
from atlasTesting.single_image_repository import SingleImageRepository

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/blocks"
# TRAINING_DATA_DIRECTORY = "../infra/training_datasets/robot-circles"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

single_image = image_repository.get_next_image()
print(image_repository.current_file)

image_repository = SingleImageRepository(single_image)

# coordinate_translator = CalibratedCoordinateTranslator(
#     VisionTableLocator().locate_table(image_repository.get_next_image()))
coordinate_translator = DummyHardcodedCoordinateTranslator()

simulator = RobotMovementSimulator(coordinate_translator)
simulator.x = 1
simulator.y = 1

motor_control = simulator
blockLocator = VisionBlockLocator()
robotLocator = simulator
obstacleLocator = VisionObstacleLocator()
objective_flag_container = ObjectiveFlagContainer()
target_zone_locator = HardcodedTargetZoneLocator()
path_planner = AStarPathPlanner()

boardFactory = FeedbackGivingBoardFactory(image_repository, blockLocator, robotLocator, obstacleLocator,
                                          coordinate_translator, objective_flag_container, target_zone_locator,
                                          GameStatus())
board = boardFactory.create_board()

board_visualization = board_to_image(board)
board_visualization.show_on_window()

obstacle_map = board.get_obstacle_map()

# target_cube = OrientedWorldCoordinate(board.cubeStorage.cubes[0].position, directions.FACING_NORTH)
target = OrientedWorldCoordinate(board.targetZones[0].position, directions.FACING_NORTH)
task = GoToTask(target, motor_control, boardFactory)

consumer = ConsoleOutputJournalMessageConsumer(LoggerFactory.get_journal())
consumer.start()

task.run()

consumer.stop()
