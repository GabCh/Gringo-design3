from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.block_detector import detect_block_with_output
from atlas.vision.colourrange import ColourRange

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/everithing-on-table3"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    image = image_repository.get_next_image()

    white = detect_block_with_output(image, ColourRange.white)
    black = detect_block_with_output(image, ColourRange.black)
    green = detect_block_with_output(image, ColourRange.green)
    # yellow = detect_block_with_output(image, ColourRange.yellow)
    red = detect_block_with_output(image, ColourRange.red)
    blue = detect_block_with_output(image, ColourRange.blue)

    image.show_on_window()