#want this to be recursive
def bfs(state):
	#currently only searches for first target
	return bfsRecursive(state, state.location[0], state.location[1], state.targets[0][0], state.targets[0][1])

#not sure if this recurses in a BFS fashion, or if I just made DFS by accident
def bfsRecursive(state, currX, currY, targetX, targetY):
	moves = state.getTransitions() #only returns valid moves from current location
	#i=0
	if len(moves) == 0:
		return "b" #b=bad path
	for move in moves:
		#check if visited, if yes ignore
		if [(move[0], move[1])] in state.visited:
			continue  
		if move[0] == targetX and move[1] == targetY:
			return state.makeMove(move[0], move[1])
 
	#makeMove function both moves the player, and saves direction moved
	direction = state.makeMove(moves[0][0], moves[0][1])
	return direction + bfsRecursive(state, state.location[0], state.location[1], targetX, targetY)

	


	