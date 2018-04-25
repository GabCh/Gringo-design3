from typing import List

from atlas.game.obstacle_map import ObstacleMap
from atlas.vision.util import PixelCoordinate


def nullHeuristic(state, problem=None):
    return 0


def manhattanHeuristic(state: PixelCoordinate, problem: "AtlasSearchProblem"):
    return abs(problem.goal.x - state.x) + abs(problem.goal.y - state.y)


class SearchProblem(object):
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        raise NotImplementedError

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        raise NotImplementedError

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        raise NotImplementedError

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        raise NotImplementedError


class AtlasSearchProblem(SearchProblem):

    def __init__(self, start: PixelCoordinate, goal: PixelCoordinate, obstacle_map: ObstacleMap):
        self.start = start
        self.goal = goal
        self.obstacle_map = obstacle_map

    def getStartState(self):
        return self.start

    def isGoalState(self, state: PixelCoordinate):
        return self.goal == state

    def getSuccessors(self, state: PixelCoordinate):
        neighbours = self.obstacle_map.get_neighbours(state.x, state.y)

        return [(neighbour, neighbour, 1) for neighbour in map(lambda tup: PixelCoordinate(tup[0], tup[1]), neighbours)]

    def getCostOfActions(self, actions: List[PixelCoordinate]):
        return len(actions)
