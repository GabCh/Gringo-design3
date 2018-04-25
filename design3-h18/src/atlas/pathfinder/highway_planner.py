from typing import List

from atlas.game.board import Board
from atlas.game.path_planner import PathPlanner
from atlas.infrastructure.stream import Stream
from atlas.pathfinder.node import Node
from atlas.pathfinder.obstacle_line import ObstacleLine
from atlas.pathfinder.orthogonal_projection_calculator import OrthogonalProjectionCalculator
from atlas.pathfinder.tree_walker import TreeWalker
from atlas.vision.util import WorldCoordinate


class HighwayPlanner(PathPlanner):

    def __init__(self, orthogonal_projection_calculator: OrthogonalProjectionCalculator, tree_walker: TreeWalker):
        self.tree_walker = tree_walker
        self.orthogonal_projection_calculator = orthogonal_projection_calculator

    def plan(self, start: WorldCoordinate, goal: WorldCoordinate, board: Board) -> List[WorldCoordinate]:

        obstacle_lines = Stream(board.obstacles).map(lambda obstacle: ObstacleLine(obstacle))
        obstacle_lines_to_cross = obstacle_lines.filter(
            lambda line: line.has_to_be_crossed_to_go_to_goal(start, goal)).toList()

        for obstacle_line in obstacle_lines_to_cross:
            for other_line in obstacle_lines_to_cross:
                if obstacle_line != other_line:
                    obstacle_line.add_neighbouring_obstacle(other_line)

        if start.y < goal.y:
            obstacle_lines_to_cross.sort(key=lambda obstacle_line: obstacle_line.y)
        else:
            obstacle_lines_to_cross.sort(key=lambda obstacle_line: obstacle_line.y, reverse=True)

        ways_across_obstacle_lines = Stream(obstacle_lines_to_cross).map(ObstacleLine.get_ways_across).toList()

        start_node = Node(start)
        nodes_on_current_line = [start_node]

        for nodes_on_next_line in ways_across_obstacle_lines:
            self.create_links(nodes_on_current_line, nodes_on_next_line, board)
            nodes_on_current_line = nodes_on_next_line

        end_node = Node(goal)
        self.create_links(nodes_on_current_line, [end_node], board)
        path = self.tree_walker.find_path(start_node, end_node)

        return Stream(path).map(lambda n: n.position).toList()

    def create_links(self, nodes_on_current_line: List[Node], nodes_on_next_line: List[Node], board: Board) -> None:
        for current_node in nodes_on_current_line:
            for potential_next_node in nodes_on_next_line:
                if self.has_line_of_sight(current_node.position, potential_next_node.position, board):
                    current_node.add_child(potential_next_node)

    def has_line_of_sight(self, point: WorldCoordinate, next_point: WorldCoordinate, board: Board) -> bool:
        line_to_next_node = next_point - point

        distance_to_obstacles = Stream(board.obstacles).map(lambda obstacle: obstacle.position - point)
        closest_point_to_obstacles = distance_to_obstacles.map(
            lambda world_delta: self.orthogonal_projection_calculator.project((world_delta.x, world_delta.y), (
                line_to_next_node.x, line_to_next_node.y))).map(
            lambda x, y: (x + point.x, y + point.y))

        points_close_to_obsacles_which_are_between_the_two_nodes = closest_point_to_obstacles.filter(
            lambda x, y: point.y < y < next_point.y or point.y > y > next_point.y)

        return points_close_to_obsacles_which_are_between_the_two_nodes.map(lambda x, y: WorldCoordinate(x, y)) \
            .noneMatch(lambda point: self.is_within_an_obstacle_radius(point, board))

    def is_within_an_obstacle_radius(self, point: WorldCoordinate, board: Board, obstacle_radius=0.20) -> bool:
        return Stream(board.obstacles).map(lambda obstacle: obstacle.position - point).anyMatch(
            lambda distance: distance.length() < obstacle_radius)
