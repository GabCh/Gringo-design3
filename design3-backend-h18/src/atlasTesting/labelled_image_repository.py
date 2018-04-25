import json

from os import path

from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.util import PixelCoordinate


class LabelledImageRepository:
    def __init__(self, training_data_path: str, labelled_data_path: str):
        self.image_repository = LocalDirectoryImageRepository(training_data_path)
        f = open(labelled_data_path)
        self.label = dict([(path.basename(key), value) for key, value in json.load(f).items()])
        f.close()

    def get_test_data_from_dataset(self) -> tuple:
        image = self.image_repository.get_next_image()
        file_name = self.image_repository.get_current_file()
        return image, self.label[file_name], file_name

    def get_robot_test_data_from_dataset(self) -> dict:
        image = self.image_repository.get_next_image()
        file_name = self.image_repository.get_current_file()
        return {
            'file-name': file_name,
            'image': image,
            'position': PixelCoordinate(*self.label[file_name]["position"]),
            'orientation': PixelCoordinate(*self.label[file_name]["front"])
        }

    def more_images(self) -> bool:
        return self.image_repository.more_images()
