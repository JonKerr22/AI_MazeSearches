from __future__ import print_function
from collections import defaultdict
import sys
import utils
from utils import accepts_tuple_arg, add_tuples
from time import sleep
from path import Path


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
        self.firstPrint = True #Utility
        self.moveDelay = moveDelay
        self.numExpanded = 0

        self.map = []
        self.location = (-1,-1)
        self.targets = []
        self.visited = defaultdict(lambda: defaultdict(bool))
        self.currentPath = []
        self.shortestPaths = defaultdict(dict)

        textFile = open(filepath)
        lines = textFile.readlines()
        for i, line in enumerate(lines):
            j = line.find('P')
            if j != -1:
                self.location = (j, i)
                self.currentPath = [(j,i)]
            line = list(line)
            self.map.append(line)
            self.targets.extend([(j,i) for j, val in enumerate(line) if val == '.'])
        self.shortestPaths[self.location] = {tuple(sorted(self.targets)):Path(None,self.location)}
        self.move(self.location, self.targets)
    @accepts_tuple_arg
    def getShortestPath(self, x, y, targets):
        return self.shortestPaths[(x,y)][tuple(sorted(targets))]
    @accepts_tuple_arg
    def updateShortestPath(self, x, y, targets, newPath):
        targets = list(targets)
        try: 
            targets.remove((x,y))
        except ValueError:
            pass
        key = tuple(sorted(targets))
        try:
            curr = self.shortestPaths[(x,y)][key]
            if len(newPath) >= len(curr):
                return
            else:
                print("\n\n\n\nNew Path")
                print(newPath)
                print(curr)
                print(self.shortestPaths[(x,y)][key].coord)
                raw_input()
                self.shortestPaths[(x,y)][key].updatePath(newPath)
                print(self.shortestPaths[(x,y)][key])
                raw_input()
                return
        except KeyError:
            pass

        self.shortestPaths[(x,y)][tuple(sorted(targets))] = newPath
            
    def getTransitions(self, *args):
        moves = [add_tuples(self.location, move) for move in POSSIBLE_MOVES]
        #notYetVisited = filter(lambda loc: self.visited[loc] != True, moves)                
        return [(coord,self.targets) for coord in moves if not self.isWall(coord)]
    @accepts_tuple_arg
    def move(self, x, y, targets):
        #assert(self.shortestPaths.get((x,y)) != None)
        targets = list(targets)
        try: 
            targets.remove((x,y))
        except ValueError:
            pass

        self.targets = targets
        key = tuple(sorted(targets))
        
        self.visited[(x,y)][key] = True
        self.location = (x,y)
        self.currentPath = self.shortestPaths[(x,y)][key]
        legalMoves = self.getTransitions()
        for move in legalMoves:
            #If we found a shorter path than the current shortest, swap it out.
            self.updateShortestPath(move[0], targets, self.currentPath+[self.location])
        self.numExpanded +=1
        if (self.moveDelay == 0):
            return
        sleep(self.moveDelay)
        self.printStatus()

###########################
############ UTILITIES ####
###########################



    def __str__(self):
        for key, value in self.shortestPaths.items():
            self.setCoord(key, len(value)%10)
        for key, value in self.visited.items():
            if value:
                self.setCoord(key, 'v')
        for coord in self.currentPath:
            self.setCoord(coord, len(self.currentPath)%10)
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
        sys.stdout.write(self.colorize()+"Current Position: " + str(self.location)+ "\nNodes expanded: "+str(self.numExpanded) + "\nPath Length: "+str(len(self.currentPath))+"\n")
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



if __name__ == "__main__":
    m1 = State("easyMaze.txt")
    m1.printStatus()
    for x in m1.currentPath:
        print(x)
