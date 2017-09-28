
def dfs(state): 
	path = ""
	totalStep = 0
	(path, totalStep) = dfsRecursive(state, state.targets[0][0], state.targets[0][1], path, totalStep)
	return (path, totalStep)

def dfsRecursive(state, targetX, targetY, path, steps):
	moves = state.getTransitions() #only returns valid moves from current location
	'''
	if steps > 100: #debugging statement
		print state.visited
		return "unfinished" + path
	
	if steps % 10 == 0: 
		print path
		i=0
	'''
	
	if len(moves) == 0:
		state.markVisited() #no path from here, dont come back
		#undo last move
		if(path[-1:] == "R"):
			state.makeMove(state.location[0] -1, state.location[1])
		elif(path[-1:] == "L"):
			state.makeMove(state.location[0] + 1, state.location[1])
		elif(path[-1:] == "U"):
			state.makeMove(state.location[0], state.location[1] +1)
		elif(path[-1:] == "D"):
			state.makeMove(state.location[0], state.location[1] - 1)
		
		path = path[:-1] 
	else:	
		for move in moves: 
			if state.atTarget(move[0], move[1], targetX, targetY):
				print "target hit"
				path+= str(state.makeMove(move[0], move[1]))
				steps+=1
				return (str(path), steps)

		#makeMove function both moves the player, direction moved
		path+= str(state.makeMove(moves[0][0], moves[0][1]))
		steps+=1
	(finalPath, steps) = dfsRecursive(state, targetX, targetY, path, steps)
	return (str(finalPath), steps)
	#return dfsRecursive(state, targetX, targetY, path, steps)