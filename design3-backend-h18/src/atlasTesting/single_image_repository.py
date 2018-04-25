from atlas.vision.image import Image
from atlas.vision.image_repository import ImageRepository


class SingleImageRepository(ImageRepository):

    def __init__(self, image: Image):
        self.image = image

    def get_next_image(self) -> Image:
        return self.image
