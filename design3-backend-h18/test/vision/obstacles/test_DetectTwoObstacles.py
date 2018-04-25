import unittest

from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.obstacle_detector import detect_obstacle, detect_obstacle_with_output

TRAINING_DATA_DIRECTORY = "../../../infra/training_datasets/demo4-scenario-with-cube-robot-and-obstacle"
test_data = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)


class TestDetectTwoObstacles(unittest.TestCase):
    def setUp(self):
        self.number_of_errors = 0
        self.number_of_tests = 0
        self.ignored_tests_cases = ['image_48.jpg', 'image_47.jpg']

    def test_givenPictures_whenThereIsTwoObstacle_thenReturnTwoPositions(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY)

        while test_data.more_images():
            data = test_data.get_next_image()
            obstacles = detect_obstacle_with_output(data)
            self.number_of_tests += 1
            file = test_data.get_current_file()
            if len(obstacles) != 2 and file not in self.ignored_tests_cases:
                self.number_of_errors += 1

                print('detect_obstacle ' + file + ' calculated: ' + str(len(obstacles)) +
                      ' required: ' + str(2))
                data.show_on_window()
        if self.number_of_errors > 0:
            self.fail(str(self.number_of_errors) + " errors in " + str(self.number_of_tests) + " tests")
        else:
            print('===Finished test for ' + str(self.number_of_tests) + ' obstacle positions.===')


if __name__ == '__main__':
    unittest.main()
