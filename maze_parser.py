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
        return func(*args, **kwargs)
    return wrapper
def add_tuples(a,b):
    return tuple([sum(x) for x in zip(a,b)])
class State:
    def __init__(self, filepath):
        self.map = []
        self.location = (-1,-1)
        self.targets = []
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
    		moves = [add_tuples((x,y), move) for move in POSSIBLE_MOVES]
        elif len(args) == 0:
        	moves = [add_tuples(self.location, move) for move in POSSIBLE_MOVES]
        
        return filter(lambda coord: not self.isWall(coord[0],coord[1]), moves)
#this class will be used to construct a connected graph from map from text file       
class Node:
	def __init__(self, coordinates, state):
		self.x = coordinates[0]
		self.y = coordinates[1]
		self.visited = False
		self.neighbors = state.getTransitions(x, y)
		self.isTarget = state.getCoord(x,y) == '.'

m1 = State("mediumMaze.txt")
print(m1)
print("Current Location: " + str(m1.location))
print("Target Locations: " +str(m1.targets))
print("Valid moves: " + str(m1.getTransitions()))
            
