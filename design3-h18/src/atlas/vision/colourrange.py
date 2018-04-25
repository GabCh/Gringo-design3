from enum import Enum
from atlas.vision.util import HsvColour
from atlas.game.Cube import CubeColour


class ColourRange(Enum):
    red = (HsvColour(0, 150, 100), HsvColour(15, 255, 255),
           HsvColour(165, 150, 100), HsvColour(180, 255, 255))
    green = (HsvColour(45, 100, 120), HsvColour(75, 255, 255))
    darkgreen = (HsvColour(45, 100, 100), HsvColour(75, 255, 255))
    blue = (HsvColour(90, 100, 100), HsvColour(130, 255, 255))
    darkblue = (HsvColour(90, 100, 50), HsvColour(130, 255, 255))
    yellow = (HsvColour(20, 100, 120), HsvColour(40, 255, 255))
    darkyellow = (HsvColour(20, 100, 100), HsvColour(40, 255, 255))
    black = (HsvColour(0, 0, 0), HsvColour(180, 255, 90))
    obstacle = (HsvColour(0, 0, 0), HsvColour(180, 255, 90))
    white = (HsvColour(0, 0, 160), HsvColour(180, 150, 255))
    white2 = (HsvColour(0, 0, 140), HsvColour(180, 150, 255))
    greenzone = (HsvColour(45, 100, 80), HsvColour(75, 255, 255))

    @staticmethod
    def translate_to_colour_range(cube_colour: int) -> "ColourRange":
        if cube_colour == CubeColour.RED:
            return ColourRange.red
        if cube_colour == CubeColour.YELLOW:
            return ColourRange.yellow
        if cube_colour == CubeColour.BLUE:
            return ColourRange.blue
        if cube_colour == CubeColour.GREEN:
            return ColourRange.green
        if cube_colour == CubeColour.BLACK:
            return ColourRange.black
        if cube_colour == CubeColour.WHITE:
            return ColourRange.white
