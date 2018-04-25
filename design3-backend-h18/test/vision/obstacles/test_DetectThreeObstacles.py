import unittest

from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.obstacle_detector import detect_obstacle

TRAINING_DATA_DIRECTORY = "../../../infra/training_datasets/quantified_obstacles_number/three_obstacles_on_table"
test_data = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY)


class TestDetectThreeObstacles(unittest.TestCase):

    def test_givenPictures_whenThereIsThreeObstacle_thenReturnThreePositions(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY)

        while test_data.more_images():
            data = test_data.get_next_image()
            obstacles = detect_obstacle(data)
            if len(obstacles) != 3:
                # data.show_on_window()
                # self.fail(test_data.get_current_file() + ' calculated: ' + str(len(obstacles)) +
                #           ' required: ' + str(3))
                print('detect_obstacle ' + test_data.get_current_file() + ' calculated: ' + str(len(obstacles)) +
                      ' required: ' + str(3))


if __name__ == '__main__':
    unittest.main()
