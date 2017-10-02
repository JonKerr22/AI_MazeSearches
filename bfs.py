from maze_parser import State
from Queue import Queue
"""
Assumption: Points on the frontier are still unexplored
Instead of backtracing, the paths should be treated as though they were moved to from the latest point
eg:
(1,2) = [a,b,c,d,e]
(x,y) = [a,b,c,f,g,h]
----
(1,2) = [a,b,c,f,g,h,g,f,c,d,e]

"""
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

def bfs(state): 
    frontier = Queue()
    for move in state.getTransitions():
    	frontier.put(move)
    while len(state.targets) > 0: 
    	curr = frontier.get()
    	state.move(curr)
        try:
            state.targets.remove(curr)
            for coord in list(frontier.queue):
                state.shortestPaths[coord] = recomputePath(state.shortestPaths[coord], state.currentPath)

        except ValueError:
            pass
    	neighbors = state.getTransitions()
    	for n in neighbors:
    		if not state.visited[n] and not n in list(frontier.queue):
    			frontier.put(n)




if __name__ == "__main__":
	m1 = State("smallSearch.txt", .1)
	bfs(m1)
