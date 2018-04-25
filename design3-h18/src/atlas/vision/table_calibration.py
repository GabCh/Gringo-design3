import numpy as np
import json
import cv2
import os

from atlas.vision.image_repository import LocalDirectoryImageRepository
from atlas.vision.goal_area_detector import detect_green_zone
from atlas.vision.table_cropper import crop_to_table_by_contours

table_objects_data = {
    'green-zone-outer': 66,
    'green-zone-inner': 59.5,
    'table-width': 231,
    'table-height': 111,
    'square-size': 2.2
}


def splitfn(fn):
    path, fn = os.path.split(fn)
    name, ext = os.path.splitext(fn)
    return path, name, ext


def get_pixel_per_cm(table: list, image) -> float:

    lenght = table[2] - table[0]
    table_ratio = (lenght / table_objects_data['table-width'])

    green_zone = detect_green_zone(image)
    gz_lenght = green_zone[len(green_zone)-1]
    green_zone_ratio = (gz_lenght / table_objects_data['green-zone-outer'])

    ratio = (green_zone_ratio + table_ratio) / 2

    return ratio / 100


def get_calibration_data(short: int =0, square_size=table_objects_data['square-size'],
                         threads_num=1, debug_dir='calibration-data/debug')-> dict:

    calibration_data = dict()

    directory = os.path.dirname(__file__)
    path = os.path.join(directory, 'calibration-data/calibration-competition')
    image_repository = LocalDirectoryImageRepository(path)
    img_names = [os.path.join(path, file) for file in image_repository.files]
    img_names.sort()
    table = crop_to_table_by_contours(image_repository.get_next_image())

    if not table:
        raise InvalidCalibration

    ratio = get_pixel_per_cm(table, image_repository.get_next_image())
    if short:
        calibration_data['pixel-m'] = ratio
        return calibration_data

    if debug_dir and not os.path.isdir(debug_dir):
        os.mkdir(debug_dir)

    pattern_size = (9, 6)
    pattern_points = np.zeros((np.prod(pattern_size), 3), np.float32)
    pattern_points[:, :2] = np.indices(pattern_size).T.reshape(-1, 2)
    pattern_points *= square_size

    obj_points = []
    img_points = []
    h, w = cv2.imread(img_names[0], 0).shape[:2]

    def processImage(fn):
        img = cv2.imread(fn, 0)
        if img is None:
            print("Failed to load", fn)
            return None

        assert w == img.shape[1] and h == img.shape[0], ("size: %d x %d ... " % (img.shape[1], img.shape[0]))
        found, corners = cv2.findChessboardCorners(img, pattern_size)
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.001)
            cv2.cornerSubPix(img, corners, (11, 11), (-1, -1), term)

        if debug_dir:
            vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            cv2.drawChessboardCorners(vis, pattern_size, corners, found)
            path, name, ext = splitfn(fn)
            outfile = os.path.join(debug_dir, name + '_chess.png')
            cv2.imwrite(outfile, vis)

        if not found:
            print('chessboard not found {}'.format(fn))
            return None

        return corners.reshape(-1, 2), pattern_points

    if threads_num <= 1:
        chessboards = [processImage(fn) for fn in img_names]
    else:
        from multiprocessing.dummy import Pool as ThreadPool
        pool = ThreadPool(threads_num)
        chessboards = pool.map(processImage, img_names)

    chessboards = [x for x in chessboards if x is not None]
    for (corners, pattern_points) in chessboards:
        img_points.append(corners)
        obj_points.append(pattern_points)

    # calculate camera distortion
    rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (w, h), None, None)
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coefs, (w, h), 1, (w, h))

    # calculate error on calibration
    mean_error = 0
    for i in range(len(obj_points)):
        imgpoints2, _ = cv2.projectPoints(obj_points[i], rvecs[i], tvecs[i], camera_matrix, dist_coefs)
        imgpoints2 = imgpoints2.reshape(-1, 2)
        error = cv2.norm(img_points[i], imgpoints2, cv2.NORM_L2) / len(imgpoints2)
        mean_error += error

    # calculate params without origin mapping
    rvecs3x3, jacob = cv2.Rodrigues(rvecs[len(rvecs) - 1])
    tvec = tvecs[len(tvecs)-1]
    rtmat = np.column_stack((rvecs3x3, tvec))
    projMat = np.matmul(camera_matrix, rtmat)

    calibration_data['newcameramtx'] = newcameramtx
    calibration_data['RMS'] = rms
    calibration_data['camera_intrinsic'] = camera_matrix
    calibration_data['distortion_coefs'] = dist_coefs.ravel()
    calibration_data['abs_error'] = (mean_error / len(obj_points))
    calibration_data['rvecs3x3'] = rvecs3x3
    calibration_data['rvecs'] = rvecs
    calibration_data['camera_extrinsic'] = rtmat
    calibration_data['tvecs'] = tvecs
    calibration_data['intrinsic_extrinsic'] = projMat
    calibration_data['pixel-m'] = ratio

    # remapping origin to fit in table corner
    matrix = calibration_data['intrinsic_extrinsic']
    m_1_transposed = np.transpose(matrix[0, :])
    m_2_transposed = np.transpose(matrix[1, :])
    m_3_transposed = np.transpose(matrix[2, :])
    world = np.array([0, 0, 0, 1])
    u = int(np.matmul(m_1_transposed, world) / np.matmul(m_3_transposed, world))
    v = int(np.matmul(m_2_transposed, world) / np.matmul(m_3_transposed, world))
    origin_x = u - table[0]
    origin_y = v - table[1]
    tvec[0] -= origin_x / square_size
    tvec[1] -= origin_y / square_size
    rtmat = np.column_stack((rvecs3x3, tvec))
    projMat = np.matmul(camera_matrix, rtmat)

    # calibration_data['camera_extrinsic'] = rtmat
    # calibration_data['intrinsic_extrinsic'] = projMat

    if calibration_data['abs_error'] > 1:
        raise InvalidCalibration
    else:
        intrinsic = calibration_data['camera_intrinsic'].tolist()
        extrinsic = calibration_data['camera_extrinsic'].tolist()
        json_file = "calibration.json"
        import codecs
        data = dict()
        data['intrinsic'] = intrinsic
        data['extrinsic'] = extrinsic
        data['coefs'] = dist_coefs.tolist()
        json.dump(data, codecs.open(json_file, 'w', encoding='utf-8'), sort_keys=True, indent=4)


class InvalidCalibration(Exception):
    pass


if __name__ == '__main__':
    get_calibration_data()
