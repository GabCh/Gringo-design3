from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.goal_area_detector import detect_green_zone

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/blocks"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    image = image_repository.get_next_image()
    positions = detect_green_zone(image)
