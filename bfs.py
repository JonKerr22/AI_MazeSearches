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
def recomputePath(originalPath, pathWithTarget):
    lastCommonIndex = len(originalPath)-1
    for i in range(len(originalPath)):
        if i == len(pathWithTarget):
            return pathWithTarget
        if originalPath[i] != pathWithTarget[i]:
            lastCommonIndex = i
            break

    return pathWithTarget + list(reversed(pathWithTarget[-lastCommonIndex:])) + originalPath[lastCommonIndex:]
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
