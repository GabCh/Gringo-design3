from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.table_highlighter import mask_environment

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/lauzon-breaking-test"
image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while image_repository.more_images():
    image = image_repository.get_next_image()
    environmentMask = mask_environment(image)
    image.apply_mask(environmentMask).show_on_window()
