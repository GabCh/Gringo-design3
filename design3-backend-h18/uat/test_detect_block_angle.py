from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.block_detector import detect_block_and_angle
from atlas.vision.colourrange import ColourRange

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/block-angles"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    image = image_repository.get_next_image()

    _, angle = detect_block_and_angle(image, ColourRange.blue)
    print(angle)

    _, angle = detect_block_and_angle(image, ColourRange.red)
    print(angle)

    _, angle = detect_block_and_angle(image, ColourRange.yellow)
    print(angle)

    image.show_on_window()
