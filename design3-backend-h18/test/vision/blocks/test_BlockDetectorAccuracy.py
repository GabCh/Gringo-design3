import unittest
import math

from atlas.vision.obstacle_detector import detect_obstacle_with_output
from atlasTesting.labelled_image_repository import LabelledImageRepository
from atlas.vision.util import PixelCoordinate
from atlas.vision.colourrange import ColourRange
from atlas.vision.block_detector import detect_block, detect_block_with_output, in_cube_storage

TRAINING_DATA_DIRECTORY = "../../../infra/training_datasets/"
LABELLED_DATA_DIRECTORY = "../../../infra/labelled_datasets/"

# DATASET_NAME = ["demo4-cube-mixed-t1", "demo4-cube-mixed-t2", "demo4-cube-obstacle-robot-t1",
#                  "demo4-cube-obstacle-robot-t2", "demo4-cube-obstacle-t1", "demo4-cube-only-t1", "demo4-cube-only-t2"]


DATASET_NAME = ["demo4-scenario-with-cube-robot-and-obstacle"]


class TestBlockDetector(unittest.TestCase):
    def setUp(self):
        self.number_of_errors = 0
        self.number_of_tests = 0

    def detectBlock(self, image, label, fn, colour):
        label_name = colour + '-block'
        colour_range = ''
        if colour == 'black':
            colour_range = ColourRange.black
        if colour == 'white':
            colour_range = ColourRange.white
        if colour == 'red':
            colour_range = ColourRange.red
        if colour == 'blue':
            colour_range = ColourRange.blue
        if colour == 'yellow':
            colour_range = ColourRange.yellow
        if colour == 'green':
            colour_range = ColourRange.green

        block_pos = detect_block_with_output(image, colour_range)
        for block in label[label_name]:
            if block[0] > 0.7*image.width and ((0 < block[1] < 0.15*image.height) or
                                               (0.85*image.height < block[1] < image.height) or
                                               (block[0] > 0.9 * image.width)):
                is_detected = False
                found_x = -1
                found_y = -1
                expected_x = block[0]
                expected_y = block[1]
                for colour_block in block_pos:
                    self.number_of_tests += 1
                    found_x = colour_block.x
                    found_y = colour_block.y

                    if math.isclose(found_x, expected_x, abs_tol=40) and math.isclose(found_y, expected_y,
                                                                                      abs_tol=40):
                        is_detected = True
                        break

                if not is_detected:
                    error_message = f"ERROR on file {fn}: colour: {colour} at position:({expected_x}, " \
                                    f"{expected_y}), found: ({found_x}, {found_y}) "
                    print(error_message)
                    image.show_on_window()
                    self.number_of_errors += 1

    def test_givenImageDataset_thenBlockPositionAndColour(self):
        for data_set in DATASET_NAME:
            training_data_directory = TRAINING_DATA_DIRECTORY + data_set
            labelled_data_directory = LABELLED_DATA_DIRECTORY + data_set
            test_data = LabelledImageRepository(training_data_directory, labelled_data_directory)

            print("===" + data_set + "====")
            while test_data.more_images():
                image, label, fn = test_data.get_test_data_from_dataset()

                self.detectBlock(image, label, fn, 'black')
                self.detectBlock(image, label, fn, 'white')
                self.detectBlock(image, label, fn, 'red')
                self.detectBlock(image, label, fn, 'blue')
                self.detectBlock(image, label, fn, 'yellow')
                self.detectBlock(image, label, fn, 'green')

        if self.number_of_errors/self.number_of_tests > 0.05:
            self.fail(str(self.number_of_errors) + " errors in " + str(self.number_of_tests) + " tests")
        else:
            print('===Finished test for ' + str(self.number_of_tests) + ' block positions.===')


if __name__ == '__main__':
    unittest.main()
