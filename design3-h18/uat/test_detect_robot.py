from atlas.vision.image_repository import LiveCapture
from atlas.vision.robot_detector import detect_robot_with_output

TRAINING_DATA_DIRECTORY = "../infra/training_datasets/robot-circles-table3"
image_repository = LiveCapture('/dev/video0')

while True:
    image = image_repository.get_next_image()

    robot = detect_robot_with_output(image)
    print(robot[1])
    image.show_and_close()
