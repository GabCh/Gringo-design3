from atlas.game.Cube import CubeColour
from atlas.game.flag import Flag

_stored_flag = [["", "", ""],
                ["RED", "WHITE", "RED"],
                ["", "", ""]]
_pattern = [row for row in map(lambda l: [j for j in map(lambda i: CubeColour.from_string(i), l)], _stored_flag)]
CANADIAN_FLAG = Flag(34, _pattern, "Canada")

_stored_flag = [
    ["BLUE", "RED", "BLUE"],
    ["RED", "WHITE", "RED"],
    ["BLUE", "RED", "BLUE"]
]
_pattern = [row for row in map(lambda l: [j for j in map(lambda i: CubeColour.from_string(i), l)], _stored_flag)]
UK_FLAG = Flag(151, _pattern, "Royaume-Uni")

_stored_flag = [
    ["RED", "BLUE", ""],
    ["BLUE", "BLUE", ""],
    ["", "", ""]
]
_pattern = [row for row in map(lambda l: [j for j in map(lambda i: CubeColour.from_string(i), l)], _stored_flag)]
AUSTRALIAN_FLAG = Flag(12, _pattern, "Australie")
