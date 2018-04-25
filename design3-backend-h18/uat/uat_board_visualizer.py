from atlas.game.BoardFactory import VisionBoardFactory
from atlas.game.game_status import GameStatus
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.vision.coordinates import DummyHardcodedCoordinateTranslator
from atlas.vision.gameboard_visualizer import board_to_image
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.vision_element_detector import VisionBlockLocator, VisionRobotLocator, VisionObstacleLocator

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/blocks"
# TRAINING_DATA_DIRECTORY = "../infra/training_datasets/robot-circles"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    print(image_repository.current_file)
    blockLocator = VisionBlockLocator()
    robotLocator = VisionRobotLocator()
    obstacleLocator = VisionObstacleLocator()
    coordinate_translator = DummyHardcodedCoordinateTranslator()
    objective_flag_container = ObjectiveFlagContainer()
    target_zone_locator = HardcodedTargetZoneLocator()

    boardFactory = VisionBoardFactory(image_repository, blockLocator, robotLocator, obstacleLocator,
                                      coordinate_translator, objective_flag_container,
                                      target_zone_locator, GameStatus())
    board = boardFactory.create_board()

    board_visualization = board_to_image(board)
    board_visualization.show_on_window()
