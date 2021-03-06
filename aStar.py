from maze_parser import State
from Queue import PriorityQueue

manhattan = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])

def aStar(state):
    frontier = PriorityQueue()
    for move in state.getTransitions():
        frontier.put((0,move))
    while not frontier.empty():
        dist, curr = tuple(frontier.get())
        position = curr[0]
        targets = list(curr[1])
        if len(targets)==0:
            break
        state.move(position, targets)
        cost = len(state.currentPath)
        state.costs[position][tuple(sorted(targets))] = cost 
        for neighbor, targets in state.getTransitions():
            if len(targets)==0:
                return
            if state.costs[neighbor][tuple(sorted(targets))] > cost+1:
                state.costs[neighbor][tuple(sorted(targets))] = cost+1
                priority = cost+heuristic(position, targets)
                frontier.put((priority,(neighbor,targets)))
            
"""    
    while (len(state.targets) > 0):
        #find the closest target
        state.targets = sorted(state.targets, key=lambda x: 
            -(MDistance(state.location, x[0], x[1])))
        currTarget = state.targets.pop()
        while (state.location != currTarget):
            neighbors = state.getTransitions()
            for neighbor in neighbors:
                if not state.visited[neighbor] and not neighbor in frontier:
                    frontier.append(neighbor)
            
            #find closest neighbor and move there (am i doing this right?)
            frontier = sorted(frontier, key=lambda x:
                -(MDistance(currTarget, x[0], x[1])))
            curr = frontier.pop()
            state.move(curr)
            
            try:
                state.targets.remove(curr)
            except ValueError:
                pass
   """

remainingDistance = {}
def computeFarthestPoints(targets):
    global remainingDistance
    key = tuple(sorted(targets))
    try:
        return remainingDistance[key]
    except KeyError:
        val = max([manhattan(pos, tar) for pos in targets for tar in targets])
        remainingDistance[key] = val
        return val
            
def heuristic(position, targets):
    #distance from position to closest target
    distance = min([manhattan(position, target) for target in targets])
    #distance to compute remaining targets
    return distance + computeFarthestPoints(targets)
def MDistance(state, goalX, goalY):
    return (abs(state[0]-goalX)+abs(state[1]-goalY))
    
if __name__ == "__main__":
    m1 = State("tinySearch.txt",0)
    targets = list(m1.targets)
    aStar(m1)
    finalPath = None
    finalPosition = (-1,-1)
    finalPathLen = -1
    for target in targets: 
        try: 
            path = m1.shortestPaths[target][()] 
            if finalPathLen == -1 or len(path) < finalPathLen: 
                finalPathLen = len(path) 
                finalPath = path 
                finalPosition = target 
        except KeyError: 
            pass 
    m1.currentPath = finalPath 
    m1.location = finalPosition 
    m1.printStatus()
