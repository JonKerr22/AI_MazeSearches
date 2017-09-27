#import maze_parser
#from maze_parser import State

def dfs(state): 
	return -1
def dfsRecursive(state, currX, currY, targetX, targetY, path, steps):
	#state.markVisited()
	moves = state.getTransitions() #only returns valid moves from current location
	if steps > 100: #debugging statement
		print state.visited
		return "unfinished" + path
	if steps % 10 == 0: 
		print path
	#i=0
	if len(moves) == 0:
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
				path+= state.makeMove(move[0], move[1])
				return path

		#makeMove function both moves the player, direction moved
		path+= (state.makeMove(moves[0][0], moves[0][1]))

	dfsRecursive(state, state.location[0], state.location[1], targetX, targetY, path, steps+1)
