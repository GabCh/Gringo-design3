from atlas.game.ConverterFactory import CalibratedTranslatorFactory
from atlas.vision.drawing import draw_crosshair
from atlas.vision.image import Image
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.obstacle_detector import detect_obstacle, detect_obstacle_with_output
from atlas.vision.util import WorldCoordinate, PixelCoordinate
from atlas.vision.vision_element_detector import VisionTableLocator

import cv2

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/new-camera-settings-table2"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)
translator = CalibratedTranslatorFactory().create_coordinate_translator()
origin = translator.world_to_pixel(WorldCoordinate(0, 0))
end = translator.pixel_to_world(PixelCoordinate(1260, 670))
while image_repository.more_images():
    image = image_repository.get_next_image()
    # undist = Image(cv2.undistort(image.frame, translator.intrinsic, translator.coefs))
    # undist.show_on_window()
    print(origin.x, origin.y)
    print(end.x, end.y)
    draw_crosshair(image, origin, [255, 0, 0])
    obstacle = detect_obstacle_with_output(image)
    for obs in obstacle:
        world = translator.pixel_to_world(obs, height=40)
        print('world coordinate: ' + str(world.x) + ' ' + str(world.y))

        pixel = translator.world_to_pixel(world)
        print('pixel coordinate: ' + str(pixel.x) + ' ' + str(pixel.y))
        cv2.circle(image.frame, (pixel.x, pixel.y), 2, (0, 0, 255), 3)
        cv2.circle(image.frame, (pixel.x, pixel.y), 30, (255, 0, 0), 3)
    image.show_on_window()
