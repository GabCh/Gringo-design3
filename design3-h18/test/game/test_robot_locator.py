import unittest

from atlas.vision.vision_element_detector import VisionRobotLocator
from atlas.vision.image_repository import LocalDirectoryImageRepository

TRAINING_DATA_DIRECTORY1 = "../../infra/training_datasets/new_robot_circles"
TRAINING_DATA_DIRECTORY2 = "../../infra/training_datasets/empty_table"
TRAINING_DATA_DIRECTORY3 = "../../infra/training_datasets/demo4-scenario-with-cube-robot-and-obstacle"
test_data = LocalDirectoryImageRepository(TRAINING_DATA_DIRECTORY3)


class RobotLocatorTest(unittest.TestCase):

    def test_givenRobotOnTable_whenGettingLocation_thenReturnIt(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY3)
        block_locator = VisionRobotLocator()
        while test_data.more_images():
            data = test_data.get_next_image()
            robot = block_locator.locate_robot(data)
            print(f"x:{robot.coordinate.x}, y:{robot.coordinate.y}")
            if robot.coordinate.x < 0 and robot.coordinate.y < 0:
                self.fail('test_givenRobotOnTable_whenGettingLocation_thenReturnIt on '
                          + test_data.get_current_file() +
                          ' calculated: NO ROBOT'
                          ' required: A ROBOT POSITION')

    def test_givenNoRobotOnTable_whenGettingLocation_thenLogIt(self):
        test_data.__init__(TRAINING_DATA_DIRECTORY2)
        block_locator = VisionRobotLocator()
        while test_data.more_images():
            data = test_data.get_next_image()
            robot = block_locator.locate_robot(data)

            if robot.coordinate.x > 0 and robot.coordinate.y > 0:
                self.fail('test_givenNoRobotOnTable_whenGettingLocation_thenLogIt on '
                          + test_data.get_current_file() +
                          ' calculated: ROBOT POSITION' +
                          ' required: NO ROBOT')


if __name__ == '__main__':
    unittest.main()
