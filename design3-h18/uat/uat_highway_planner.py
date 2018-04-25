from atlas.game.Cube import CubeColour
from atlas.game.game_status import GameStatus
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.game.objective_flag_container import ObjectiveFlagContainer
from atlas.motor.robot_movement_simulator import RobotMovementSimulator
from atlas.pathfinder.highway_planner import HighwayPlanner
from atlas.pathfinder.orthogonal_projection_calculator import OrthogonalProjectionCalculator
from atlas.pathfinder.tree_walker import TreeWalker, CannotFindPathException
from atlas.vision.coordinates import CalibratedCoordinateTranslator
from atlas.vision.drawing import draw_crosshair
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.vision_element_detector import VisionBlockLocator, VisionObstacleLocator
from atlasTesting.feedback_giving_board_factory import FeedbackGivingBoardFactory
from atlasTesting.single_image_repository import SingleImageRepository

# TRAINING_DATA_DIRECTORY = "../infra/training_datasets/blocks"
# TRAINING_DATA_DIRECTORY = "../infra/training_datasets/robot-circles"
TRAINING_DATA_DIRECTORY = "../infra/training_datasets/tricky-path-planning"
base_image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while base_image_repository.more_images():
    single_image = base_image_repository.get_next_image()
    print(base_image_repository.current_file)

    image_repository = SingleImageRepository(single_image)

    coordinate_translator = CalibratedCoordinateTranslator()

    blockLocator = VisionBlockLocator()
    robot_locator = RobotMovementSimulator(coordinate_translator)
    obstacleLocator = VisionObstacleLocator()
    objective_flag_container = ObjectiveFlagContainer()
    target_zone_locator = HardcodedTargetZoneLocator()

    boardFactory = FeedbackGivingBoardFactory(image_repository, blockLocator, robot_locator, obstacleLocator,
                                              coordinate_translator, objective_flag_container, target_zone_locator,
                                              GameStatus())
    board = boardFactory.create_board()

    planner = HighwayPlanner(OrthogonalProjectionCalculator(), TreeWalker())

    try:
        plan = planner.plan(board.robot.position, board.cubeStorage.get_cube_position(CubeColour.RED)[0].coordinate,
                            board)

        image = image_repository.get_next_image()

        for obstacle in board.obstacles:
            pixel_coordinate = coordinate_translator.world_to_pixel(obstacle.position)
            draw_crosshair(image, pixel_coordinate, [0, 255, 0], size=20)

        for i in plan:
            pixel_coordinate = coordinate_translator.world_to_pixel(i)
            draw_crosshair(image, pixel_coordinate, [255, 0, 0], size=20)

        for target in board.targetZones:
            pixel_coordinate = coordinate_translator.world_to_pixel(target.position)
            draw_crosshair(image, pixel_coordinate, [0, 127, 255], size=20)

        image.show_on_window()
    except CannotFindPathException:
        print("Could not find path.")
        continue
