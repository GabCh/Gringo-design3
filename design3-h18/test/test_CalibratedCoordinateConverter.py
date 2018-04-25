import math
import unittest

from atlas.game.ConverterFactory import CalibratedTranslatorFactory
from atlas.vision.block_detector import detect_block_with_output
from atlas.vision.colourrange import ColourRange
from atlas.vision.drawing import draw_crosshair
from atlas.vision.util import WorldCoordinate
from atlasTesting.labelled_image_repository import LabelledImageRepository

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/cube-distance-t2"
LABELLED_DATA_DIRECTORY = "../infra/labelled_datasets/cube-distance-t2"


class CalibratedConverterTest(unittest.TestCase):

    def setUp(self):
        self.converter = CalibratedTranslatorFactory().create_coordinate_translator()
        self.origin = self.converter.world_to_pixel(WorldCoordinate(0, 0))
        self.number_of_errors = 0
        self.number_of_tests = 0

    def test_givenBlocksInCorner_whenPixelCoordinatesFound_thenReturnAccurateWorldCoordinate(self):
        test_data = LabelledImageRepository(TRAINING_DATA_DIRECTORY, LABELLED_DATA_DIRECTORY)

        while test_data.more_images():
            image, label, _ = test_data.get_test_data_from_dataset()
            draw_crosshair(image, self.origin, [255, 0, 0])
            world_pos = []
            for positions in label['world-positions']:
                world_pos.append(WorldCoordinate(positions[0], positions[1]))

            red_blocks = detect_block_with_output(image, ColourRange.red)
            blue_blocks = detect_block_with_output(image, ColourRange.blue)
            blocks = red_blocks + blue_blocks
            i = 0
            for block in blocks:
                block_world = self.converter.pixel_to_world(block)
                self.number_of_tests += 1
                if math.isclose(abs(block_world.x), world_pos[i].x, abs_tol=0.03) \
                        and math.isclose(block_world.y, world_pos[i].y, abs_tol=0.03):
                    i += 1
                else:
                    error_message = f"calculated: [{block_world.x}, {block_world.y}] required: [{world_pos[i].x}, " \
                                    f"{world_pos[i].y}] "
                    print(error_message)
                    self.number_of_errors += 1
        if self.number_of_errors > 0:
            self.fail(str(self.number_of_errors) + " errors in " + str(self.number_of_tests) + " tests")
        else:
            print('===Finished test for ' + str(self.number_of_tests) + ' block positions.===')


if __name__ == '__main__':
    unittest.main()
