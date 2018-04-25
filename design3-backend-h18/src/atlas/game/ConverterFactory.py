from atlas.vision.coordinates import CalibratedCoordinateTranslator, CoordinateTranslator, \
    DummyHardcodedCoordinateTranslator
from atlas.vision.image_repository import ImageRepository
from atlas.vision.util import PixelCoordinate


class CoordinateTranslatorFactory(object):
    def create_coordinate_translator(self):
        raise NotImplementedError


class CalibratedTranslatorFactory(CoordinateTranslatorFactory):

    def create_coordinate_translator(self):
        return CalibratedCoordinateTranslator()


class RatioTranslatorFactory(CoordinateTranslatorFactory):

    def __init__(self, image_repository: ImageRepository, pixel_width: int, world_width: float,
                 origin: PixelCoordinate):
        self.image_repository = image_repository
        self.pixel_width = pixel_width
        self.world_width = world_width
        self.origin = origin

    def create_coordinate_translator(self):
        return CoordinateTranslator(self.pixel_width, self.world_width, self.origin)


class DummyTranslatorFactory(CoordinateTranslatorFactory):

    def create_coordinate_translator(self):
        return DummyHardcodedCoordinateTranslator()


calibrated_coordinate_translator = None


def get_calibrated_coordinate_translator() -> CalibratedCoordinateTranslator:
    global calibrated_coordinate_translator
    if calibrated_coordinate_translator is None:
        calibrated_coordinate_translator = \
            CalibratedTranslatorFactory().create_coordinate_translator()
    return calibrated_coordinate_translator
