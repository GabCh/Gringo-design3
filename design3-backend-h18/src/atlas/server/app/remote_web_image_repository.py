import base64
import io

import PIL.Image
import cv2
import numpy as np

from atlas.vision.image import Image
from atlas.vision.image_repository import ImageRepository


class RemoteWebImageRepository(ImageRepository):

    def __init__(self):
        self.currentImage = Image(np.zeros((1, 1, 3), dtype="uint8"))

    def add_image(self, data_uri: str):
        n_arr = self.convert_to_arr(data_uri)
        self.currentImage = Image(n_arr)

    def get_next_image(self) -> Image:
        return self.currentImage

    def set_image_from_base64_numpy_array(self, array: str):
        array = eval(array)
        array = base64.decodebytes(array)
        np_arr = np.frombuffer(array, dtype=np.uint8)
        np_arr = np_arr.reshape((720, 1280, 3))
        self.currentImage = Image(np_arr)

    @staticmethod
    def convert_to_arr(data_uri):
        b64_str = data_uri.split(',')[1]
        buf = io.BytesIO()
        buf.write(base64.b64decode(b64_str))
        img = PIL.Image.open(buf)
        n_arr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        return n_arr
