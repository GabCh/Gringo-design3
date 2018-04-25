import unittest

from atlas.vision.vision_element_detector import VisionObstacleLocator
from atlas.vision.image_repository import LocalDirectoryImageRepository

TRAINING_DATA_DIRECTORY1 = "../../infra/training_datasets/quantified_obstacles_number/two_obstacles_on_table"
TRAINING_DATA_DIRECTORY2 = "../../infra/training_datasets/empty_table"
test_data = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY1)


class ObstacleLocatorTest(unittest.TestCase):

    def test_givenTwoObstaclesOnTable_whenGettingLocation_thenReturnThem(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY1)
        block_locator = VisionObstacleLocator()
        while test_data.more_images():
            data = test_data.get_next_image()
            obstacles = block_locator.locate_obstacles(data)

            if len(obstacles) != 2:
                self.fail('test_givenTwoObstaclesOnTable_whenGettingLocation_thenReturnThem on '
                          + test_data.get_current_file() +
                          ' calculated: ' + str(len(obstacles)) +
                          ' required: ' + str(1))

    def test_givenNoObstacle_whenGettingLocation_thenLogIt(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY2)
        block_locator = VisionObstacleLocator()
        while test_data.more_images():
            data = test_data.get_next_image()
            obstacles = block_locator.locate_obstacles(data)

            if len(obstacles) != 0:
                self.fail('test_givenNoObstacle_whenGettingLocation_thenLogIt on '
                          + test_data.get_current_file() +
                          ' calculated: ' + str(len(obstacles)) +
                          ' required: ' + str(0))


if __name__ == '__main__':
    unittest.main()
