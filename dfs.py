
def dfs(state): 
	path = "sadfasd"
	print typeof(path)
	path = dfsRecursive(state, state.location[0], state.location[1], state.targets[0][0], state.targets[0][1], "", 0)
	return path

def dfsRecursive(state, currX, currY, targetX, targetY, path, steps):
	print path
	moves = state.getTransitions() #only returns valid moves from current location
	#print moves
	if steps > 100: #debugging statement
		print state.visited
		return "unfinished" + path
	if steps % 10 == 0: 
		#print path
		i=0
	#i=0
	if len(moves) == 0:
		print "undoing at: " + str(state.location)

		state.markVisited() #no path from here, dont come back
		#undo last move
		if(path[-1:] == "R"):
			state.makeMove(currX -1, currY)
		elif(path[-1:] == "L"):
			state.makeMove(currX + 1, currY)
		elif(path[-1:] == "U"):
			state.makeMove(currX, currY -1)
		elif(path[-1:] == "D"):
			state.makeMove(currX, currY + 1)
		
		path = path[:-1] #remove last char
	else:	
		for move in moves: 
			if move[0] == targetX and move[1] == targetY:
				path+= str(state.makeMove(move[0], move[1]))
				return path

		#makeMove function both moves the player, direction moved
		path+= str(state.makeMove(moves[0][0], moves[0][1]))

	dfsRecursive(state, state.location[0], state.location[1], targetX, targetY, path, steps+1)
