from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.block_detector import detect_block_with_output
from atlas.vision.colourrange import ColourRange

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/new-camera-settings-table2"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    image = image_repository.get_next_image()

    position = detect_block_with_output(image, ColourRange.black)
    position = detect_block_with_output(image, ColourRange.blue)
    position = detect_block_with_output(image, ColourRange.green)
    position = detect_block_with_output(image, ColourRange.red)
    position = detect_block_with_output(image, ColourRange.yellow)
    position = detect_block_with_output(image, ColourRange.white)

    image.show_on_window()


