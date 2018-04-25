import math

import cv2

import atlas.vision.colourspace as colourspace
from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate, HsvColour

ROBOT_CIRCLES_NUMBER = 3


def detect_robot(bgr_image: Image) -> list:
    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_mask = hsv_image.get_in_range_mask(HsvColour(160, 100, 180).colour, HsvColour(180, 170, 255).colour)
    higher_mask = hsv_image.get_in_range_mask(HsvColour(0, 100, 180).colour, HsvColour(8, 170, 255).colour)
    mask = lower_mask + higher_mask
    output_image = hsv_image.apply_mask(mask)
    opened_image = output_image.erode_rect(5).dilate_rect(5)
    gray_image = colourspace.hsv_to_gray(opened_image)
    im, contours, hierarchy = gray_image.find_contours()

    circles = filter_found_circles_by_size(contours)
    if len(circles) >= ROBOT_CIRCLES_NUMBER:
        front, back_right, back_left = find_front_and_back(circles)

        center_of_mass, theta = find_angle_and_center(front, back_right, back_left)
        return [PixelCoordinate(center_of_mass[0], center_of_mass[1]), theta]
    else:
        return []


def detect_robot_with_output(bgr_image: Image) -> list:
    hsv_image = colourspace.bgr_to_hsv(bgr_image)
    lower_mask = hsv_image.get_in_range_mask(HsvColour(160, 100, 180).colour, HsvColour(180, 170, 255).colour)
    higher_mask = hsv_image.get_in_range_mask(HsvColour(0, 100, 180).colour, HsvColour(8, 170, 255).colour)
    mask = lower_mask + higher_mask
    output_image = hsv_image.apply_mask(mask)
    opened_image = output_image.erode_rect(5).dilate_rect(5)
    gray_image = colourspace.hsv_to_gray(opened_image)
    im, contours, hierarchy = gray_image.find_contours()

    circles = filter_found_circles_by_size(contours)
    if len(circles) >= ROBOT_CIRCLES_NUMBER:
        front, back_right, back_left = find_front_and_back(circles)

        center_of_mass, theta = find_angle_and_center(front, back_right, back_left)

        p1 = center_of_mass[0] - 40, center_of_mass[1]
        p2 = center_of_mass[0] + 40, center_of_mass[1]

        cv2.circle(bgr_image.frame, center_of_mass, 2, (255, 0, 0), 2)
        cv2.line(bgr_image.frame, back_right, front, (255, 0, 0), 2)
        cv2.line(bgr_image.frame, back_right, back_left, (255, 0, 0), 2)
        cv2.line(bgr_image.frame, back_left, front, (255, 0, 0), 2)
        cv2.line(bgr_image.frame, p1, p2, (0, 255, 0), 2)
        cv2.line(bgr_image.frame, center_of_mass, front, (0, 255, 0), 2)
        return [PixelCoordinate(center_of_mass[0], center_of_mass[1]), theta]
    else:
        return []


def filter_found_circles_by_size(contours: list) -> list:
    contours.sort(key=lambda blob: cv2.boundingRect(blob)[0])

    circles = []
    for c in contours:
        (x, y), r = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))
        r = int(r)

        if 10 <= r <= 30:
            circles.append(center)

    return circles


def find_front_and_back(circles: list) -> tuple:
    last_circle = circles[len(circles) - 1]

    distances = []
    points = []

    for circle in circles:
        dist = int(math.sqrt(math.pow(circle[0] - last_circle[0], 2) + math.pow(circle[1] - last_circle[1], 2)))
        distances.append(dist)
        points.append((circle, last_circle))

        last_circle = circle

    min_dist = min(distances)
    back_left, back_right = points[distances.index(min_dist)]

    max_dist = max(distances)
    front, front2 = points[distances.index(max_dist)]

    if front == back_left or front == back_right:
        front = front2

    cross_prod = ((back_left[0] - back_right[0]) * (front[1] - back_right[1]) - (back_left[1] - back_right[1]) * (
            front[0] - back_right[0]))

    if cross_prod < 0:
        temp = back_left
        back_left = back_right
        back_right = temp

    return front, back_right, back_left


def find_angle_and_center(front: tuple, back_right: tuple, back_left: tuple) -> tuple:
    delta_x = back_right[0] - back_left[0]
    delta_y = back_left[1] - back_right[1]

    theta = math.atan2(delta_y, delta_x)
    theta *= 180 / math.pi
    theta -= 90

    center_of_mass = (int((back_right[0] + back_left[0] + front[0]) / 3),
                      int((back_right[1] + back_left[1] + front[1]) / 3))

    if theta < 0:
        theta = theta + 360

    return center_of_mass, theta
