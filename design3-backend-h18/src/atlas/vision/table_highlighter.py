from typing import List, Callable

import numpy as np

from atlas.vision import colourspace
from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate, Mask


def mask_environment(bgr_image: Image, *, saturation_threshold=50, value_threshold=50) -> Mask:
    center_line = [PixelCoordinate(i, bgr_image.height // 2 - 1) for i in range(0, bgr_image.width - 1)]
    hsv_image = colourspace.bgr_to_hsv(bgr_image)

    average_hsv = _compute_pixel_average_color(hsv_image, center_line)

    focus_mask = np.ones((bgr_image.height, bgr_image.width), dtype="uint8")

    ray_tracer = PixelLineMaskTracer(hsv_image,
                                     lambda colour: _is_exceeding_threshold(colour, average_hsv,
                                                                                 saturation_threshold,
                                                                                 value_threshold))
    for pixel in center_line:
        ray_tracer.mask_environment(focus_mask, pixel, PixelCoordinate.north)
        ray_tracer.mask_environment(focus_mask, pixel, PixelCoordinate.south)

    return Mask(focus_mask)


def _compute_pixel_average_color(image: Image, pixels: List[PixelCoordinate]) -> np.array:
    accumulator = np.array([0, 0, 0], dtype="uint64")
    for pixel in pixels:
        accumulator += image[pixel]
    return np.array(accumulator / len(pixels), dtype="uint8")


def _is_exceeding_threshold(pixel_hsv: np.array, baseline_average: np.array, saturation_threshold: int,
                            value_threshold: int) -> bool:
    return pixel_hsv[1] > baseline_average[1] + saturation_threshold \
           or pixel_hsv[2] < baseline_average[2] - value_threshold


class PixelLineMaskTracer:
    def __init__(self, image: Image, exceeds_threshold_function: Callable):
        self.image = image
        self.exceeds_threshold = exceeds_threshold_function

    def mask_environment(self, mask: np.array, starting_pixel: PixelCoordinate, pixel_direction_iterator: Callable) -> None:
        pixel_on_vertical_line = starting_pixel

        first_pixel_exceeding_threshold = None
        has_been_exceeding_threshold_for = 0

        is_under_threshold_since = 0

        while self.image.contains(pixel_on_vertical_line):
            if self.exceeds_threshold(self.image[pixel_on_vertical_line]):
                if first_pixel_exceeding_threshold is None:
                    first_pixel_exceeding_threshold = pixel_on_vertical_line
                else:
                    has_been_exceeding_threshold_for += 1
                if has_been_exceeding_threshold_for > 12:
                    pixel_on_vertical_line = first_pixel_exceeding_threshold
                    break
            else:
                is_under_threshold_since += 1
                if is_under_threshold_since > 7:
                    has_been_exceeding_threshold_for = 0
                    first_pixel_exceeding_threshold = None

            pixel_on_vertical_line = pixel_direction_iterator(pixel_on_vertical_line)

        while self.image.contains(pixel_on_vertical_line):
            mask[pixel_on_vertical_line.y, pixel_on_vertical_line.x] = 0
            pixel_on_vertical_line = pixel_direction_iterator(pixel_on_vertical_line)
