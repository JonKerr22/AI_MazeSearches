from maze_parser import State

def greedy(state):
    frontier = []
    
    while (len(state.targets) > 0):
        #find the closest target

        state.targets = sorted(state.targets, key=lambda x: 
            -(MDistance(state.location, x[0], x[1])))
        currTarget = state.targets.pop()
        while (state.location != currTarget):

            neighbors = state.getTransitions()
            for neighbor in neighbors:
                if not state.visited[neighbor] and not neighbor in frontier:
                    frontier.append(neighbor)
            
            #find closest neighbor and move there (am i doing this right?)
            frontier = sorted(frontier, key=lambda x:
                -(MDistance(currTarget, x[0], x[1])))
            curr = frontier.pop()
            state.move(curr)
            
            try:
                state.targets.remove(curr)
            except ValueError:
                pass
        
def MDistance(state, goalX, goalY):
    return (abs(state[0]-goalX)+abs(state[1]-goalY))
    
if __name__ == "__main__":
    m1 = State("mediumMaze.txt", 0)
    greedy(m1)
    m1.printStatus()
