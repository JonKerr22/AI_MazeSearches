import bfs, dfs, greedy, aStar
from bfs import bfs 
from dfs import dfs
from greedy import greedySearch
from aStar import aStarSearch

#all the vars we will need
#convetions, upper right is (0,0) coordinate
#state = {location =(x,y), targets {(x1,y1), (x2,y2)...}}
#some sort of way of keeping track of where we visited, probably just change actual maze
#a way to save the actual path we end up taking in order to save it

#maze is going to be a 2d char array
#useful functions, getNeighbors to get a set of coords back on status of neighbors
#			printMaze(show a pic of maze currently)
#			Manhattan distance		

#transitions, are just moving 1 either up down left or right, count # of steps
# for part 2 at least, we need to remove visited targets
# keep a set of what we've vistited 

POSSIBLE_MOVES = [(-1,0),(1,0),(0,-1),(0,1)]
def accepts_tuple_arg(func):
    def wrapper(*args, **kwargs):
        #args = map(lambda arg: (arg[0],arg[1] if isinstance(arg,tuple) else arg), args)
        #placeholder while I work on this
        temp = []
        for arg in args:
            if isinstance(arg,tuple):
                temp += [coord for coord in arg]
            else:
                temp.append(arg)
        return func(*temp, **kwargs)
    return wrapper
def add_tuples(a,b):
    return tuple([sum(x) for x in zip(a,b)])
class State:
    def __init__(self, filepath):
        self.map = []
        self.location = (-1,-1)
        self.targets = []
        self.visited = []
        textFile = open(filepath)
        lines = textFile.readlines()
        for i, line in enumerate(lines):
            j = line.find('P')
            if j != -1:
                self.location = (j, i)
            line = list(line)
            self.map.append(line)
            self.targets.extend([(j,i) for j, val in enumerate(line) if val == '.'])
    def __str__(self):
        return ''.join([''.join(row) for row in self.map])
    @accepts_tuple_arg
    def getCoord(self, x, y):
        return self.map[y][x]
    def isWall(self, x, y):
        return self.getCoord(x,y) == '%'
    def getTransitions(self, *args):
    	if len(args) == 2:
    		moves = [add_tuples((self.location[0],self.location[1]), move) for move in POSSIBLE_MOVES]
        elif len(args) == 0:
        	moves = [add_tuples(self.location, move) for move in POSSIBLE_MOVES]

        #print str(moves)
        #try:
    	#input("Press enter to continue")

		#except:
    	#	pass
        #TODO: filter out visited locations as well, maybe
        '''
        print str(moves)
        for move in moves:
        	print str(move)
        	print str(self.visited)
        	if move in self.visited:
        		print str(move) + "visited, so removed from" +str(moves)
        		moves.remove(move)
        		print "new moves: " + str(moves)
        '''
        notYetVisited = filter(lambda loc: loc not in self.visited, moves)
        
        return filter(lambda coord: not self.isWall(coord[0],coord[1]), notYetVisited)
    #just orders lowest to highest x values, 
    #this is definitely a bad hueristic, 
    #just a placeholder for now	    
    def reorderTargets(self):
    	if len(self.targets) > 1:
    		self.targets.sort()
    def currentMDistance(self):
    	return abs(self.location[0] - self.targets[0][0]) + abs(self.location[1] - self.targets[0][1])
    def allMDistnaces(self):
    		distances = []
    		for i in range(len(self.targets)):
    			distances.append(abs(self.location[0] - self.targets[i][0]) + abs(self.location[1] - self.targets[i][1]))
    		return distances

    #assuming only valid moves with step cost 1 will be passed into this function
    def makeMove(self, newX, newY):
    	#mark current spot as visited, I'm not sure how we want to do this
    	self.markVisited()

    	direction = "" #used to keep track of overall path taken
    	if(self.location[0] != newX):
    		if(self.location[0] < newX):
    			direction = "R"
    		else:
    			direction = "L"
    	elif(self.location[1] != newY):
    		if(self.location[1] < newY):
    			direction = "D"
    		else:
    			direction = "U"

    	self.location = (newX, newY)
    	return direction
    #simple list of tuples for visited, we might need to change format for larger mazes
    def markVisited(self):
    	self.visited.append((self.location[0], self.location[1]))
    def visitCheck(self):
    	return [self.location[0], self.location[1]] in self.visited
    def visitedSpots(self):
    	return self.visited

#this class will be used to construct a connected graph from map from text file       
class Node:
	def __init__(self, coordinates, state):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.visited = False
		self.neighbors = state.getTransitions(self.x, self.y)
		self.isTarget = state.getCoord(self.x,self.y) == '.'
		#distance from the first target
		self.manhattanDistance = abs(self.x - state.targets[0][0]) + abs(self.y - state.targets[0][1])
		

	#def onNode(self):
	#	self.visited = True
	#def unvisit(self):


m1 = State("bigMaze.txt")
#startNode = Node((m1.location[0],m1.location[1]),m1)
print(m1)
print("Current Location: " + str(m1.location))
print("Target Locations: " +str(m1.targets))
print("Valid moves: " + str(m1.getTransitions()))
#print("curr Mdistances " + str(m1.allMDistnaces()))
#m1.reorderTargets()
#print("reordered targets " + str(m1.targets))
print " "
a = str(dfs(m1)) 
print("Path taken:\n" + a + "\nStep Cost: " + str(len(a)) )

print(m1.getCoord(0,0))
print(m1.getCoord((0,0)))
