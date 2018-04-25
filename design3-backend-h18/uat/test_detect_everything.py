from atlas.game.ConverterFactory import CalibratedTranslatorFactory
from atlas.vision.image_repository import LocalDirectoryImageRepository, LiveCapture
from atlas.vision.robot_detector import detect_robot_with_output
from atlas.vision.block_detector import detect_block_with_output
from atlas.vision.obstacle_detector import detect_obstacle_with_output
from atlas.vision.colourrange import ColourRange
import cv2 as cv

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/demo4-cube-obstacle-robot-t2"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)
translator = CalibratedTranslatorFactory().create_coordinate_translator()

while image_repository.more_images():
    image = image_repository.get_next_image()

    robot = detect_robot_with_output(image)
    white = detect_block_with_output(image, ColourRange.white)
    black = detect_block_with_output(image, ColourRange.black)
    red = detect_block_with_output(image, ColourRange.red)
    green = detect_block_with_output(image, ColourRange.green)
    blue = detect_block_with_output(image, ColourRange.blue)
    yellow = detect_block_with_output(image, ColourRange.yellow)

    obstacles = detect_obstacle_with_output(image)
    for obs in obstacles:
        world = translator.pixel_to_world(obs, height=40)
        pixel = translator.world_to_pixel(world)
        cv.circle(image.frame, (pixel.x, pixel.y), 2, (0, 0, 255), 3)
        cv.circle(image.frame, (pixel.x, pixel.y), 30, (255, 0, 0), 3)

    if robot:
        print(robot[1])
        robot_position = translator.world_to_pixel(translator.pixel_to_world(robot[0], height=30))
        cv.circle(image.frame, (robot_position.x, robot_position.y), 5, (0, 0, 255), -1)
        cv.circle(image.frame, (robot_position.x, robot_position.y), 80, (255, 0, 0), 2)
    image.show_on_window()



