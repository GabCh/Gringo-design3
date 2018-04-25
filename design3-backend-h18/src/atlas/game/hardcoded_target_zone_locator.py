from typing import List

from atlas.game.element_detectors import TargetZoneLocator
from atlas.vision.image import Image
from atlas.vision.util import WorldCoordinate


class HardcodedTargetZoneLocator(TargetZoneLocator):

    def locate_target_zones(self, image: Image) -> List[WorldCoordinate]:
        target_zones = []
        for i in range(0, 3):
            for j in range(2, -1, -1):
                target = WorldCoordinate(0.27 + j * 0.27, 0.28 + i * 0.27)
                target_zones.append(target)

        return target_zones
