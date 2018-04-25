from atlas.vision.util import WorldCoordinate


class Node(object):

    def __init__(self, position: WorldCoordinate):
        self.position = position
        self.children = []

    def add_child(self, node: "Node"):
        self.children.append(node)
