
def dfs(state): 
	path = ""
	print type(path)
	path = str(dfsRecursive(state, state.location[0], state.location[1], state.targets[0][0], state.targets[0][1], "", 0))
	print path
	return path

def dfsRecursive(state, currX, currY, targetX, targetY, path, steps):
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
		#print "already visited: " + str(state.visited)
		#print "undoing at: " + str(state.location)

		state.markVisited() #no path from here, dont come back
		#undo last move
		if(path[-1:] == "R"):
			state.makeMove(currX -1, currY)
		elif(path[-1:] == "L"):
			state.makeMove(currX + 1, currY)
		elif(path[-1:] == "U"):
			state.makeMove(currX, currY +1)
		elif(path[-1:] == "D"):
			state.makeMove(currX, currY - 1)
		
		path = path[:-1] #remove last char
	else:	
		for move in moves: 
			if move[0] == targetX and move[1] == targetY:
				print "target hit"
				path+= str(state.makeMove(move[0], move[1]))
				print type(path)
				
				return str(path)

		#makeMove function both moves the player, direction moved
		path+= str(state.makeMove(moves[0][0], moves[0][1]))

	dfsRecursive(state, state.location[0], state.location[1], targetX, targetY, path, steps+1)
