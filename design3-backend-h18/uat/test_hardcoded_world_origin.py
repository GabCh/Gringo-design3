from atlas.game.world_origin_detector import HardCodedOriginDetector
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.drawing import draw_crosshair

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/720p_high_def"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)
origin_detector = HardCodedOriginDetector()

while image_repository.more_images():
    image = image_repository.get_next_image()
    origin = origin_detector.find_origin(image)
    draw_crosshair(image, origin, [255, 0, 255])
    image.show_on_window()
