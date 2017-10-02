from maze_parser import State
from Queue import Queue
def bfs(state): 
    initialTargets = list(state.targets)
    frontier = Queue()
    for move in state.getTransitions():
    	frontier.put(move)
    while len(frontier.queue) > 0: 
    	curr = frontier.get()
        position = curr[0]
        targets = list(curr[1])
        if (len(targets)==0):
            continue
        state.move(position, targets)
        neighbors = state.getTransitions()
        for neighbor, targets in neighbors:
            if state.visited[neighbor][tuple(sorted(targets))]:
                state.updateShortestPath(neighbor,targets,state.currentPath)
            elif not (neighbor,targets) in frontier.queue:
                frontier.put((neighbor,targets))
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
    m1 = State("mediumMaze.txt",.01)

    bfs(m1)
