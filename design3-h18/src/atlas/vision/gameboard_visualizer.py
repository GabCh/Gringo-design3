import numpy as np

from atlas.game.board import Board
from atlas.game.obstacle_map import ObstacleMap
from atlas.vision.drawing import draw_crosshair
from atlas.vision.image import Image
from atlas.vision.util import PixelCoordinate


def board_to_image(board: Board) -> Image:
    image = Image(np.zeros((120, 250, 3), dtype="uint8"))
    for block in board.cubeStorage.cubes:
        draw_crosshair(image, PixelCoordinate(int(block.position.y * 100), int(block.position.x * 100)),
                       colour=[255, 0, 0])  # block = blue

    for obstacle in board.obstacles:
        draw_crosshair(image, PixelCoordinate(int(obstacle.position.y * 100), int(obstacle.position.x * 100)),
                       colour=[0, 255, 0])  # obstacle = Green

    draw_crosshair(image, PixelCoordinate(int(board.robot.position.y * 100), int(board.robot.position.x * 100)),
                   colour=[210, 0, 255])  # Pink = robot

    for target_zone in board.targetZones:
        draw_crosshair(image, PixelCoordinate(int(target_zone.position.y * 100), int(target_zone.position.x * 100)),
                       colour=[0, 144, 255]) # Orange = target zones

    return image


def obstacle_map_to_image(obstacle_map: ObstacleMap) -> Image:
    image_matrix = np.copy(obstacle_map.matrix)
    image_matrix[image_matrix == 1] = 255
    image = Image(image_matrix)
    return image
