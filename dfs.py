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


Unsustainable. This will roughly double the path length
"""
#Computes a path from a to b
def recomputePath(a, b):
    a_reverse = list(reversed(a))
    b_reverse = list(reversed(b))
    shortestPathLen = len(a)+len(b)
    bestI = 0
    bestJ = 0
    for i, x in enumerate(a_reverse):
        if i > shortestPathLen:
            break
        j = -1
        try:
            j = b_reverse[:shortestPathLen-i].index(x)
        except ValueError:
            continue
        pathLen = i + j
        if pathLen < shortestPathLen:
            shortestPathLen = pathLen
            bestI = i
            bestJ = j
    return a + a_reverse[1:bestI] + b[-bestJ:]
        
def dfs(state):
    global minPathLength
    frontier = []
    frontier += state.getTransitions()
    finalPath = []
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

