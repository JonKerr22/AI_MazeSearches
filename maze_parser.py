from __future__ import print_function
from collections import defaultdict
import sys
import utils
from time import sleep

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
    def __init__(self, filepath, moveDelay = .5):
        self.map = []
        self.location = (-1,-1)
        self.targets = []
        self.firstPrint = True
        self.visited = defaultdict(bool)
        self.finalPath = []
        self.currentPath = []
        """
        Each square on the frontier maintains a list of the paths used to reach it
        If the current path is shorter than the stored one, 
        """
        self.shortestPaths = {}
        self.moveDelay = moveDelay
        textFile = open(filepath)
        lines = textFile.readlines()
        for i, line in enumerate(lines):
            j = line.find('P')
            if j != -1:
                self.location = (j, i)
                self.shortestPaths[self.location] = [(j,i)]
                self.currentPath = [(j,i)]
            line = list(line)
            self.map.append(line)
            self.targets.extend([(j,i) for j, val in enumerate(line) if val == '.'])
        self.move(self.location)

    def __str__(self):
        for key, value in self.shortestPaths.items():
            self.setCoord(key, len(value)%10)
        for key, value in self.visited.items():
            if value:
                self.setCoord(key, 'v')
        for coord in self.currentPath:
            self.setCoord(coord, '.')
        self.setCoord(self.location, 'P')
        return ''.join([''.join(row) for row in self.map])
    def colorize(self):
        string = str(self)
        string = string.replace('%', utils.lightGrayBG('%'))
        string = string.replace('.', utils.greenText('.'))
        string = string.replace('P', utils.cyanText('P'))
        string = string.replace('v', utils.darkGrayBG('v'))
        return string
    def printStatus(self):
        maze_height = len(self.map)
        if self.firstPrint:
            self.firstPrint = False
        else:
            scrollUp(maze_height+3)
        sys.stdout.write(self.colorize() + 
                         "\nCurrent Location: " + str(self.location) + 
                         "\nTarget Locations: " +str(self.targets) + 
                         "\nValid moves: " + str(self.getTransitions()) + "\n")
        sys.stdout.flush()
    @accepts_tuple_arg
    def getCoord(self, x, y):
        return self.map[y][x]
    @accepts_tuple_arg
    def setCoord(self, x, y, val):
        self.map[y][x] = str(val)
    @accepts_tuple_arg    
    def isWall(self, x, y):
        return self.getCoord(x,y) == '%'
    def getTransitions(self, *args):
        if len(args) == 2:
            moves = [add_tuples((x,y), move) for move in POSSIBLE_MOVES]
        elif len(args) == 0:
            moves = [add_tuples(self.location, move) for move in POSSIBLE_MOVES]
        #notYetVisited = filter(lambda loc: self.visited[loc] != True, moves)                
        return [coord for coord in moves if not self.isWall(coord)]
    @accepts_tuple_arg
    def move(self, x, y):
        assert(self.shortestPaths.get((x,y)) != None)
        self.visited[(x,y)] = True
        self.location = (x,y)
        self.currentPath = self.shortestPaths[(x,y)]
        legalMoves = self.getTransitions()
        for move in legalMoves:
            #If we found a shorter path than the current shortest, swap it out.
            if self.shortestPaths.get(move) == None or len(self.shortestPaths[move]) > len(self.currentPath):
                self.shortestPaths[move] = self.currentPath + [(x,y)]
                
        """
        assert(legalMoves.index((x,y)) != -1)
        self.location = (x,y)
        self.visited[(x,y)] = True
        self.finalPath.append((x,y))
        """
        sleep(self.moveDelay)
        self.printStatus()
    def backtrace(self): #unused
        self.finalPath.pop()
        self.location = self.finalPath[-1]
        sleef(self.moveDelay)
        self.printStatus()

#this class will be used to construct a connected graph from map from text file       
class Node:
    def __init__(self, coordinates, state):
        self.x, self.y = coordinates
        self.visited = False
        self.neighbors = state.getTransitions(x, y)
        self.isTarget = state.getCoord(x,y) == '.'

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
    #simple list of tuples for visited, we might need to change format for larger mazes
    def markVisited(self):
    	self.visited[self.location] = True
    def visitCheck(self):
    	return self.visited == True
    def visitedSpots(self):
    	return self.visited

if __name__ == "__main__":
    m1 = State("easyMaze.txt")
    m1.printStatus()
    m1.move(23,1)
    m1.move(23,2)
    m1.move(22,2)
