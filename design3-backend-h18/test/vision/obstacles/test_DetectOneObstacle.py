import unittest

from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.obstacle_detector import detect_obstacle, detect_obstacle_with_output

TRAINING_DATA_DIRECTORY = "../../../infra/training_datasets/quantified_obstacles_number/one_obstacle_on_table"
test_data = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)


class TestDetectOneObstacle(unittest.TestCase):

    def test_givenPictures_whenThereIsOneObstacle_thenReturnOnePosition(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY)

        while test_data.more_images():
            data = test_data.get_next_image()
            obstacles = detect_obstacle_with_output(data)
            if len(obstacles) != 1:
                self.fail(test_data.get_current_file() + ' calculated: ' + str(len(obstacles)) +
                          ' required: ' + str(1))


if __name__ == '__main__':
    unittest.main()
