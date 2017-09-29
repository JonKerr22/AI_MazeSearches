from maze_parser import State
from Queue import Queue

#want this to be recursive
def bfs(state): 
    frontier = Queue()
    for move in state.getTransitions():
    	frontier.put(move)
    while len(state.targets) > 0: 
    	curr = frontier.get()
    	state.move(curr)
    	neighbors = state.getTransitions()
    	for n in neighbors:
    		if not state.visited[n] and not n in list(frontier.queue):
    			frontier.put(n)
    	try:
            state.targets.remove(curr)
        except ValueError:
            pass


if __name__ == "__main__":
	m1 = State("smallSearch.txt", .1)
	bfs(m1)
