import json
import unittest

from atlas.server.app import RemoteWebImageRepository
from atlas.vision.image import Image


class RemoteWebImageRepositoryTest(unittest.TestCase):
    IMAGE_DATA = 'image_data.json'

    def setUp(self):
        with open(self.IMAGE_DATA) as fd:
            self.images_uri = json.load(fd)['items']

    def test_givenEmptyQueue_whenAddingImageAndRequest_thenImageReturn(self):
        image_uri = self.images_uri[0]

        remote_direct = RemoteWebImageRepository()
        remote_direct.add_image(image_uri)
        image_in = Image(RemoteWebImageRepository.convert_to_arr(image_uri))
        image_out = remote_direct.get_next_image()

        self.assertEqual(image_in.frame.all(), image_out.frame.all())

    def test_givenAFullQueue_whenAddingImage_thenPopOldestImage(self):
        remote_direct = RemoteWebImageRepository()

        for idx, image_uri in enumerate(self.images_uri):
            remote_direct.add_image(image_uri)
        image_num_idx_1 = Image(RemoteWebImageRepository.convert_to_arr(self.images_uri[1]))
        image_out = remote_direct.get_next_image()

        self.assertEqual(image_num_idx_1.frame.all(), image_out.frame.all())

    def test_givenOnlyOneImage_whenAskingForTwoImages_thenReturnTheLastOne(self):
        remote_direct = RemoteWebImageRepository()
        image_uri = self.images_uri[0]

        remote_direct.add_image(image_uri)
        image_requested_1 = remote_direct.get_next_image()
        image_requested_2 = remote_direct.get_next_image()

        self.assertEqual(image_requested_1.frame.all(), image_requested_2.frame.all())


if __name__ == "__main__":
    unittest.main()
