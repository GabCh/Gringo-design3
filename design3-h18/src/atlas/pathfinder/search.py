from atlas.pathfinder.problem import nullHeuristic
from atlas.pathfinder.queue import PriorityQueue


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    """Implemente d'apres le pseudo-code de wikipedia: https://en.wikipedia.org/wiki/A*_search_algorithm"""
    closedSet = set()

    openSet = PriorityQueue()

    # Priority is fscore
    openSet.push(problem.getStartState(), 0)

    cameFrom = {}
    gScore = {}
    gScore[problem.getStartState()] = 0


    while not openSet.isEmpty():
        current = openSet.pop()
        if problem.isGoalState(current):
            return reconstruct_path(cameFrom, current)

        closedSet.add(current)

        for neighbour, action, cost in problem.getSuccessors(current):
            if neighbour in closedSet:
                continue

            tentative_gScore = gScore[current] + cost
            if neighbour in gScore and tentative_gScore >= gScore[neighbour]:
                continue

            cameFrom[neighbour] = current, action
            gScore[neighbour] = tentative_gScore
            openSet.push(neighbour, gScore[neighbour] + heuristic(neighbour, problem))
    return []

def reconstruct_path(cameFrom, current):
    """Implemente d'apres le pseudo-code de wikipedia: https://en.wikipedia.org/wiki/A*_search_algorithm"""
    total_path = [current]
    while current in cameFrom.keys():
        current,action = cameFrom[current]
        total_path.append(action)
    total_path.reverse()
    return total_path[:-1]
