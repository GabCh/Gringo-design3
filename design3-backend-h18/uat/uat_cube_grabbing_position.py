from atlas.game.Cube import CubeColour, Cube
from atlas.vision.coordinates import CalibratedCoordinateTranslator
from atlas.vision.vision_element_detector import VisionBlockLocator, VisionTableLocator
from atlasTesting.labelled_image_repository import LabelledImageRepository

image_repo = LabelledImageRepository("../infra/training_datasets/cube-grabbing",
                                     "../infra/labelled_datasets/cube-grabbing")

while image_repo.more_images():
    image, label = image_repo.get_test_data_from_dataset()

    block_locator = VisionBlockLocator()
    blocks = block_locator.locate_blocks(image, CubeColour.RED)
    table = VisionTableLocator().locate_table(image)
    coordinate_translator = CalibratedCoordinateTranslator(table)

    cubes = [cube for cube in
             map(lambda pixel: Cube(coordinate_translator.pixel_to_world(pixel), CubeColour.RED), blocks)]

    print(label['red'], cubes[0].get_grab_orientation(), cubes[0].position)
