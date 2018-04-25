from typing import List

from atlas.pathfinder.node import Node


class TreeWalker(object):

    def find_path(self, start_node: Node, end_node: Node) -> List[Node]:
        visited = set()
        stack = [start_node]
        came_from = {}
        while len(stack) > 0:
            current_node = stack.pop(0)
            visited.add(current_node)
            for child in current_node.children:
                if child not in visited:
                    stack.append(child)
                    came_from[child] = current_node
                    if child == end_node:
                        break

        if end_node not in came_from:
            raise CannotFindPathException()
        path = []
        node = end_node
        while node is not None:
            path.append(node)
            node = came_from.get(node)
        path.append(start_node)
        return path[::-1]


class CannotFindPathException(Exception):
    pass
