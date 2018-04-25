import math

import cv2
import numpy as np

from atlas.vision import colourspace
from atlas.vision.image import Image
from atlas.vision.table_cropper import crop_to_table_by_contours
from atlas.vision.util import PixelCoordinate
from atlas.vision.colourrange import ColourRange


def detect_green_zone(bgr_image: Image) -> list:

    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_bound = ColourRange.greenzone.value[0]
    upper_bound = ColourRange.greenzone.value[1]

    lower_mask = hsv_image.get_in_range_mask(lower_bound.colour, upper_bound.colour)

    mask = lower_mask

    output_image = hsv_image.apply_mask(mask)
    gray_image = colourspace.hsv_to_gray(output_image)
    binary_image = gray_image.binary_threshold(0, 180)

    results, green_zone = filter_contours(binary_image, bgr_image, bgr_image.width / 5, bgr_image.width / 1.5)

    return results


def detect_green_zone_with_output(bgr_image: Image) -> list:

    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_bound = ColourRange.greenzone.value[0]
    upper_bound = ColourRange.greenzone.value[1]

    lower_mask = hsv_image.get_in_range_mask(lower_bound.colour, upper_bound.colour)

    mask = lower_mask

    output_image = hsv_image.apply_mask(mask)
    gray_image = colourspace.hsv_to_gray(output_image)
    binary_image = gray_image.binary_threshold(0, 180)

    results, green_zone = filter_contours(binary_image, bgr_image, bgr_image.width / 5, bgr_image.width / 1.5)

    for zone in green_zone:
        if type(zone) is tuple:
            cv2.circle(bgr_image.frame, zone, 5, (255, 0, 0), 2)

    return results


def filter_contours(binary_image: Image, bgr_image: Image, min_width: int, max_width: int, table=None, trim=0) -> tuple:

    im, contours, hierarchy = binary_image.find_contours()

    results = []
    green_zone = []
    for contour in contours:
        if shape_matches_width(contour, min_width, max_width):

            rc = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rc)
            sum_x = 0
            sum_y = 0

            for p in box:
                pt = (p[0], p[1])
                green_zone.append(pt)
                sum_x += pt[0]
                sum_y += pt[1]

            if table is not None:
                moy_x = int(sum_x / 4) + table[0]
                moy_y = int(sum_y / 4) + table[1] + trim
                results.append(PixelCoordinate(moy_x, moy_y))
            else:
                moy_x = int(sum_x / 4)
                moy_y = int(sum_y / 4)

                if is_point_on_table(bgr_image, moy_x, moy_y):
                    results.append(PixelCoordinate(moy_x, moy_y))
            x, y, w, h = cv2.boundingRect(contour)
            green_zone.append(w)

    if green_zone:
        results.append(green_zone.pop())
    return results, green_zone


def shape_matches_width(contour: np.ndarray, min_width: int, max_width: int) -> bool:

    perimeter_max = max_width * 4
    perimeter_min = min_width * 4

    rc = cv2.minAreaRect(contour)

    box = cv2.boxPoints(rc)

    box_width = math.sqrt(math.pow(box[1][0] - box[0][0], 2) + math.pow(box[1][1] - box[0][1], 2))
    box_height = math.sqrt(math.pow(box[2][0] - box[1][0], 2) + math.pow(box[2][1] - box[1][1], 2))
    perimeter = cv2.arcLength(contour, True)
    if math.isclose(box_width, box_height, rel_tol=0.7) \
            and perimeter_min < perimeter < perimeter_max:
        return True

    return False


def is_point_on_table(bgr_image: Image, x: int, y: int) -> bool:
    rect = crop_to_table_by_contours(bgr_image)

    table = np.array([[rect[0], rect[1]], [rect[0], rect[3]], [rect[2], rect[3]], [rect[2], rect[1]]])

    if cv2.pointPolygonTest(table, (x, y), False) >= 0:
        return True

    return False