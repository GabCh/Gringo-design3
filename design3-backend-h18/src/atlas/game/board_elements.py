from atlas.vision.util import WorldCoordinate, OrientedWorldCoordinate


class Localizable(object):
    def __init__(self, position: WorldCoordinate):
        self.position = position

    def get_position(self):
        return self.position


class TargetZone(Localizable):

    def __init__(self, position: WorldCoordinate):
        Localizable.__init__(self, position)
        self.isOccupied = False

    def set_occupied(self):
        self.isOccupied = True


class Robot(Localizable):

    def __init__(self, position: OrientedWorldCoordinate):
        Localizable.__init__(self, position.coordinate)
        self.angle = position.angle


class Obstacle(Localizable):

    def __init__(self, position: WorldCoordinate):
        Localizable.__init__(self, position)
