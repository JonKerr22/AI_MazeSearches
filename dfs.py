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
    m1 = State("mediumMaze.txt",.1)
    dfs(m1)
