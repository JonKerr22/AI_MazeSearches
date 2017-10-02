from collections import defaultdict
from maze_parser import State
def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))
"""
Assumption: Points on the frontier are still unexplored
Instead of backtracing, the paths should be treated as though they were moved to from the latest point
eg:
(1,2) = [a,b,c,d,e]
(x,y) = [a,b,c,f,g,h]
----
(1,2) = [a,b,c,f,g,h,g,f,c,d,e]

"""
def recomputePath(originalPath, pathWithTarget):
    lastCommonIndex = len(originalPath)-1
    for i in range(len(originalPath)):
        if originalPath[i] != pathWithTarget[i]:
            lastCommonIndex = i
            break

    return pathWithTarget + list(reversed(pathWithTarget[-lastCommonIndex:])) + originalPath[lastCommonIndex:]
   
def dfs(state):
    frontier = []
    frontier += state.getTransitions()
    while len(state.targets) > 0:
        curr = frontier.pop()
        state.move(curr)
        try:
            state.targets.remove(curr)
            for coord in frontier:
                state.shortestPaths[coord] = recomputePath(state.shortestPaths[coord], state.currentPath)
        except ValueError:
            pass
        neighbors = state.getTransitions()
        for neighbor in neighbors:
            if not state.visited[neighbor] and not neighbor in frontier:
                frontier.append(neighbor)
if __name__ == "__main__":
    m1 = State("smallSearch.txt",.1)
    dfs(m1)

