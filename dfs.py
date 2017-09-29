<<<<<<< HEAD
from maze_parser import State
def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))
def dfs(state):
    frontier = []
    frontier += state.getTransitions()
    while len(state.targets) > 0:
        curr = frontier.pop()
        state.move(curr)
        neighbors = state.getTransitions()
        for neighbor in neighbors:
            if not state.visited[neighbor] and not neighbor in frontier:
                frontier.append(neighbor)
        try:
            state.targets.remove(curr)
        except ValueError:
            pass
if __name__ == "__main__":
    m1 = State("smallSearch.txt",.1)
    dfs(m1)
=======
def dfs(state, wayOption): 
	path = ""
	totalStep = 0
	if wayOption == 1:
		(path, totalStep) = dfsRecursive_oneWay(state, state.targets[0][0], state.targets[0][1], path, totalStep)
	elif wayOption == 2:
		(path, totalStep) = dfs_twoWay(state, state.targets[0][0], state.targets[0][1], path, totalStep)
	else:
		print "pick either 1 or 2 for search directions"
		return ("-1", -1)
	return (path, totalStep)

def dfsRecursive_oneWay(state, targetX, targetY, path, steps):
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

		#makeMove function both moves the player, retuns direction moved
		path+= str(state.makeMove(moves[0][0], moves[0][1]))
		steps+=1
	(finalPath, steps) = dfsRecursive_oneWay(state, targetX, targetY, path, steps)
	return (str(finalPath), steps)

def dfs_twoWay(state, targetX, targetY, path, steps):
	reverseState = state.makeCopy()
	reverseState.targets = reverseState.location
	reverseState.location = (targetX, targetY)

	print("reversed start location: " + str(reverseState.location))
	print("reversed start target: " + str(reverseState.targets))
	pathF = ""
	pathB = ""
	(pathF, pathB, steps) = dfsRecursive_twoWay(state, reverseState, pathF, pathB, steps)
	path = pathF + pathB
	return (path,steps)

def dfsRecursive_twoWay(stateF, stateB, pathF, pathB, steps):
	fMoves = stateF.getTransitions()
	bMoves = stateB.getTransitions()
	if len(fMoves) == 0:
		stateF.markVisited() 
		if(pathF[-1:] == "R"):
			stateF.makeMove(stateF.location[0] -1, stateF.location[1])
		elif(pathF[-1:] == "L"):
			stateF.makeMove(stateF.location[0] +1, stateF.location[1])
		elif(pathF[-1:] == "U"):
			stateF.makeMove(stateF.location[0], stateF.location[1] +1)
		elif(pathF[-1:] == "D"):
			stateF.makeMove(stateF.location[0], stateF.location[1] -1)
		
		pathF = pathF[:-1] 
	elif len(bMoves) == 0:
		print(pathB)
		stateB.markVisited()#no path from here, dont come back
		#undo last move
		if(pathB[0] == "R"):
			stateB.makeMove(stateB.location[0] -1, stateB.location[1])
		elif(pathB[-1:] == "L"):
			stateB.makeMove(stateB.location[0] +1, stateB.location[1])
		elif(pathB[-1:] == "U"):
			stateB.makeMove(stateB.location[0], stateB.location[1] +1)
		elif(pathB[-1:] == "D"):
			stateB.makeMove(stateB.location[0], stateB.location[1] -1)

		pathB = pathB[1:]
	else:	
		for move in fMoves: 
			if stateF.atTarget(move[0], move[1], stateB.location[0], stateB.location[1]):
				print "target hit"
				pathF+= str(stateF.makeMove(move[0], move[1]))
				steps+=1
				return (str(pathF), str(pathB), steps)

		#makeMove function both moves the player, returns direction moved
		pathF+= str(stateF.makeMove(fMoves[0][0], fMoves[0][1]))
		pathB = str(stateB.makeMove(bMoves[0][0], bMoves[0][1])) + pathB
		steps+=2
	(pathF, pathB, steps) = dfsRecursive_twoWay(stateF, stateB, pathF, pathB, steps)
	return (str(pathF), str(pathB), steps)
>>>>>>> 161a165d387b6424945b037e31027164c205aa79
