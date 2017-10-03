from collections import defaultdict
from maze_parser import State
def printFrontier(frontier):
    print("Frontier: "+str([coord[0] for coord in frontier]))
def dfs(state):
    initialTargets = list(state.targets)
    frontier = []
    frontier += state.getTransitions()
    while len(frontier) > 0:
        curr = frontier.pop()
        position = curr[0]
        targets = list(curr[1])
        if (len(targets)==0):
            continue
        state.move(position, targets)
        for key, path in state.shortestPaths.items():
            for k, p in path.items():
                print("Key {0} Path {1}".format(key, p))
        neighbors = state.getTransitions()
        print("Current path")
        print(state.currentPath)
        for neighbor, targets in neighbors:
            if state.visited[neighbor][tuple(sorted(targets))]:
                #state.updateShortestPath(neighbor,targets,state.currentPath)
                pass
            elif not (neighbor,targets) in frontier:
                frontier.append((neighbor,targets))
        printFrontier(frontier)
        raw_input()
    #For all the final states, find the one with the shortest path
    finalPath = None
    finalPosition = (-1,-1)
    finalPathLen = -1
    for target in initialTargets:
        try:
            path = state.shortestPaths[target][()]
            if finalPathLen == -1 or len(path) < finalPathLen:
                finalPathLen = len(path)
                finalPath = path
                finalPosition = target
        except KeyError:
            pass
    state.currentPath = finalPath
    state.location = finalPosition
    state.printStatus()
if __name__ == "__main__":
    m1 = State("testSearch.txt",.1)
    dfs(m1)

