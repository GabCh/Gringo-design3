import cv2
import atlas.vision.colourspace as colourspace

from atlas.vision.image import Image

OFFSET_Y = 0
OFFSET_X = 0
THRESHOLDS = [140, 120, 100, 80]


def crop_to_table_by_colour(bgr_image: Image) -> Image:
    white_lower = [0, 0, 60]
    white_higher = [180, 30, 100]

    hsv_image = colourspace.bgr_to_hsv(bgr_image)

    mask = hsv_image.get_in_range_mask(white_lower, white_higher)

    masked_image = hsv_image.apply_mask(mask)
    masked_image.show_on_window()


def find_rectangle(gray_image: Image, offset_x: int, offset_y: int, thresh=140) -> list:
    image_binary = gray_image.binary_threshold(thresh, 255)
    open_image = image_binary.erode_rect(5).dilate_rect(5)
    im, contours, hierarchy = open_image.find_contours()
    # Trouve la plus grosse zone
    if not contours:
        return []
    cnt = contours[0]
    max_area = cv2.contourArea(cnt)

    for cont in contours:
        if cv2.contourArea(cont) > max_area:
            cnt = cont
            max_area = cv2.contourArea(cont)

    # Trouve le contour approx.

    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    cv2.drawContours(gray_image.frame, approx, 2, [255, 0, 0], 2)
    # gray_image.show_on_window()
    # Trouve le rectangle englobant maximum
    max_x = 0
    max_y = 0
    min_x = 9999
    min_y = 9999

    for a in approx:
        if max_x <= a[0][0]:
            max_x = a[0][0]
        if min_x >= a[0][0]:
            min_x = a[0][0]

        if max_y <= a[0][1]:
            max_y = a[0][1]
        if min_y >= a[0][1]:
            min_y = a[0][1]

    min_y -= offset_y
    max_x += offset_x
    max_y += offset_y
    return [min_x, min_y, max_x, max_y]


def crop_to_table_by_contours(image: Image, offset_x=OFFSET_X, offset_y=OFFSET_Y, crop_into_table=0) -> list:
    # return [25, 65, 1270, 685]  # IN CASE OF EMERGENCY
    gray_image = colourspace.bgr_to_gray(image)
    for thresh in THRESHOLDS:

        rect = find_rectangle(gray_image, offset_x, offset_y, thresh=thresh)

        # Validate if table is located at a sane position in image
        if rect and rect[0] < 75:
            if crop_into_table > 0:
                rect[1] += crop_into_table
                rect[3] -= crop_into_table
            return rect

        return rect
    raise CannotFindTableException()


def crop_table_from_masked_environement(image: Image):
    opened = image.erode_rect(7).dilate_rect(7)
    min_x = image.width
    min_y = image.height
    max_x = 0
    max_y = 0
    x = 0
    y = 0

    offset_x = 10
    offset_y = 20

    while x < image.width:
        while y < image.height:

            if opened.frame[y][x][0] != 0 and opened.frame[y][x][1] != 0 \
                    and opened.frame[y][x][2] != 0:

                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y

                if x > max_x:
                    max_x = x
                if max_y < y < (image.height - offset_y):
                    max_y = y

            y = y + 1

        y = 0
        x = x + 1

    return [min_x - offset_x, min_y - offset_y, max_x + offset_x, max_y + offset_y]


class CannotFindTableException(Exception):
    pass
