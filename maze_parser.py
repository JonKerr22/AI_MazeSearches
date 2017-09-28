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
from __future__ import print_function
import sys
from time import sleep
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

##Ignore these functions. They are utilities for printing to console
def scrollUp(n=1):
    for i in range(0,n):
        sys.stdout.write('\x1b[1A')
        sys.stdout.flush()

def scrollDown(n=1):
    for i in range(0,n):
        sys.stdout.write('\n')
        sys.stdout.flush()
class State:
    def __init__(self, filepath):
        self.map = []
        self.location = (-1,-1)
        self.targets = []
        self.firstPrint = True
        self.visited = {}
        self.finalPath = []
        textFile = open(filepath)
        lines = textFile.readlines()
        for i, line in enumerate(lines):
            j = line.find('P')
            if j != -1:
                self.location = (j, i)
                self.finalPath = [(j,i)]
            line = list(line)
            self.map.append(line)
            self.targets.extend([(j,i) for j, val in enumerate(line) if val == '.'])
    def __str__(self):
        for key, value in self.visited.items():
            self.setCoord(key, 'v')
        for coord in self.finalPath:
            self.setCoord(coord, '.')
        self.setCoord(self.location, 'P')
        return ''.join([''.join(row) for row in self.map])
    def printStatus(self):
        maze_height = len(self.map)
        if self.firstPrint:
            self.firstPrint = False
        else:
            scrollUp(maze_height+3)
        sys.stdout.write(str(self) + 
                         "\nCurrent Location: " + str(m1.location) + 
                         "\nTarget Locations: " +str(m1.targets) + 
                         "\nValid moves: " + str(m1.getTransitions()) + "\n")
        sys.stdout.flush()
    @accepts_tuple_arg
    def getCoord(self, x, y):
        return self.map[y][x]
    @accepts_tuple_arg
    def setCoord(self, x, y, val):
        self.map[y][x] = val
    @accepts_tuple_arg    
    def isWall(self, x, y):
        return self.getCoord(x,y) == '%'
    def getTransitions(self, *args):
        if len(args) == 2:
            moves = [add_tuples((x,y), move) for move in POSSIBLE_MOVES]
        elif len(args) == 0:
            moves = [add_tuples(self.location, move) for move in POSSIBLE_MOVES]
        
        return [coord for coord in moves if not self.isWall(coord)]
    @accepts_tuple_arg
    def move(self, x, y):
        legalMoves = self.getTransitions()
        assert(legalMoves.index((x,y)) != -1)
        self.location = (x,y)
        self.visited[(x,y)] = True
        self.finalPath.append((x,y))
    def backtrace(self):
        self.finalPath.pop()
        self.location = self.finalPath[-1]
#this class will be used to construct a connected graph from map from text file       
class Node:
	def __init__(self, coordinates, state):
		self.x, self.y = coordinates
		self.visited = False
		self.neighbors = state.getTransitions(x, y)
		self.isTarget = state.getCoord(x,y) == '.'

m1 = State("mediumMaze.txt")
#print(m1)
#print("Current Location: " + str(m1.location))
#print("Target Locations: " +str(m1.targets))
#print("Valid moves: " + str(m1.getTransitions()))
            
#m1.printStatus()
m1.printStatus()
sleep(.5)
m1.move(2,21)
m1.printStatus()
sleep(.5)
m1.move(3,21)
m1.printStatus()
m1.backtrace()
sleep(.5)
m1.printStatus()
print(m1.finalPath.pop())
print(m1.finalPath)
