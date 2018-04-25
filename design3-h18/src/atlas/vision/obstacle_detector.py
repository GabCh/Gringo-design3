from typing import List

import cv2
import numpy as np

import atlas.vision.colourspace as colourspace
from atlas.infrastructure.stream import Stream
from atlas.vision.colourrange import ColourRange
from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate, HsvColour


def detect_obstacle(bgr_image: Image):
    results, bases = detect_circles_by_colour(bgr_image, *ColourRange.obstacle.value)
    return results


def detect_obstacle_with_output(bgr_image: Image):
    results, bases = detect_circles_by_colour(bgr_image, *ColourRange.obstacle.value)
    radius = 50
    for result in results:
        cv2.circle(bgr_image.frame, (result.x, result.y), radius, (0, 255, 0), 2)
        cv2.circle(bgr_image.frame, (result.x, result.y), 2, (0, 0, 255), 3)

    return results


def detect_circles_by_colour(bgr_image: Image, lower_bound: HsvColour,
                             higher_bound: HsvColour) -> tuple:
    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_mask = hsv_image.get_in_range_mask(lower_bound.colour, higher_bound.colour)
    mask = lower_mask
    output_image = hsv_image.apply_mask(mask)
    blacked_image = output_image.binary_threshold(50, 180)
    gray_image = colourspace.bgr_to_gray(blacked_image)

    circles = cv2.HoughCircles(gray_image.frame, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=25, minRadius=30, maxRadius=50)

    results = remove_overlapping_circles(circles)
    # TODO remove or tweak this sanity check
    results = Stream(results).filter(lambda obstacle_position: obstacle_position.x < 1200 and
                                    0.1 * bgr_image.height < obstacle_position.y < 0.9 * bgr_image.height).toList()

    results, bases = find_base(results, bgr_image)

    return results, bases


def remove_overlapping_circles(circles: np.array) -> List[PixelCoordinate]:
    potential_obstacles = []

    if circles is not None:
        pixel_circle = np.uint16(np.around(circles))
        potential_obstacles = Stream(pixel_circle[0, :]).map(lambda x, y, _: PixelCoordinate(x, y)).toList()

    non_overlapping_obstacles = []
    for obstacle in potential_obstacles:
        has_an_overlapping_neighbour = False
        for other_obstacle in non_overlapping_obstacles:
            if obstacle.isclose(other_obstacle, delta=80):
                has_an_overlapping_neighbour = True
                break
        if not has_an_overlapping_neighbour:
            non_overlapping_obstacles.append(obstacle)

    return non_overlapping_obstacles


def find_base(results: list, image: Image) -> tuple:
    bases = []
    for result in results:
        percentage_x = -1 * (result.x - (image.width / 2)) / (image.width * 5)
        percentage_y = -1 * (result.y - (image.height / 2)) / (image.height * 5)

        base_x = result.x + percentage_x * image.width
        base_y = result.y + percentage_y * image.height

        bases.append(PixelCoordinate(int(base_x), int(base_y)))

    return results, bases
