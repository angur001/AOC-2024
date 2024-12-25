maze = [[char for char in line] for line in open("input.txt", "r").read().splitlines()]

def get_start():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                return i, j
            
def get_end():
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "E":
                return i, j
            
start = get_start()
end = get_end()

def get_neighbors(pos):
    i, j = pos
    neighbors = []
    if i > 0 and maze[i - 1][j] != "#":
        neighbors.append((i - 1, j))
    if i < len(maze) - 1 and maze[i + 1][j] != "#":
        neighbors.append((i + 1, j))
    if j > 0 and maze[i][j - 1] != "#":
        neighbors.append((i, j - 1))
    if j < len(maze[i]) - 1 and maze[i][j + 1] != "#":
        neighbors.append((i, j + 1))
    return neighbors


def bfs(start_pos):
    global start, end
    queue = [(start_pos, 0, "horizontal", set())]
    score = 1000000000000000
    while queue:
        pos, _score, direction, visited = queue.pop(0)
        # print_position_in_maze(pos)
        # print(f"score is {_score}")
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            score = min(score, _score) 
            continue
        for neighbor in get_neighbors(pos):
            if neighbor in visited:
                continue
            if direction == "horizontal":
                if neighbor[0] == pos[0]:
                    queue.append((neighbor, _score + 1, "horizontal", visited.copy()))
                else:
                    queue.append((neighbor, _score + 1001, "vertical", visited.copy()))
            else:
                if neighbor[1] == pos[1]:
                    queue.append((neighbor, _score + 1, "vertical", visited.copy()))
                else:
                    queue.append((neighbor, _score + 1001, "horizontal", visited.copy()))
    return score

def print_position_in_maze(pos):
    i, j = pos
    for k in range(len(maze)):
        for l in range(len(maze[k])):
            if k == i and l == j:
                print("X", end="")
            else:
                print(maze[k][l], end="")
        print()

print(bfs(start))
        

    

