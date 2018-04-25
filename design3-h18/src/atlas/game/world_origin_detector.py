from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate


class WorldOriginDetector:

    def find_origin(self, image: Image) -> PixelCoordinate:
        raise NotImplementedError


class HardCodedOriginDetector(WorldOriginDetector):

    def find_origin(self, image: Image) -> PixelCoordinate:
        return PixelCoordinate(343, 363)
