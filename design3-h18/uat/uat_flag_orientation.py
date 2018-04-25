from atlas.game.board_elements import TargetZone
from atlas.game.hardcoded_target_zone_locator import HardcodedTargetZoneLocator
from atlas.infrastructure.stream import Stream
from atlas.vision import colourrange
from atlas.vision.coordinates import CalibratedCoordinateTranslator
from atlas.vision.drawing import draw_crosshair
from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlasTesting.testing_flag import AUSTRALIAN_FLAG

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/tricky-path-planning"
base_image_repository = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)

while base_image_repository.more_images():
    single_image = base_image_repository.get_next_image()
    flag = AUSTRALIAN_FLAG
    hardcoded_target_zone_locator = HardcodedTargetZoneLocator()
    zones = Stream(hardcoded_target_zone_locator.locate_target_zones(None)).map(
        lambda position: TargetZone(position)).toList()
    cube_requests = flag.get_cube_requests(zones)

    for cube_request in cube_requests:
        colour = colourrange.ColourRange.translate_to_colour_range(cube_request.blockColour)
        pixel_coordinate = CalibratedCoordinateTranslator().world_to_pixel(cube_request.drop_position)
        draw_crosshair(single_image, pixel_coordinate, colour.value[0].colour)

    single_image.show_on_window()
