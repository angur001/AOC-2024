grid = [[elem for elem in line.strip()] for line in open('input.txt')]

def get_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                return (i, j)
            
def get_end(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'E':
                return (i, j)
            
start = get_start(grid)
end = get_end(grid)

def get_neighbors(grid, pos):
    i, j = pos
    neighbors = []
    if i > 0 and grid[i-1][j] != '#':
        neighbors.append((i-1, j))
    if i < len(grid) - 1 and grid[i+1][j] != '#':
        neighbors.append((i+1, j))
    if j > 0 and grid[i][j-1] != '#':
        neighbors.append((i, j-1))
    if j < len(grid[i]) - 1 and grid[i][j+1] != '#':
        neighbors.append((i, j+1))
    return neighbors

def get_race_track(grid, start, end):
    visited = []
    queue = [start]
    while queue:
        pos = queue.pop(0)
        visited.append(pos)
        if pos == end:
            return visited
        neighbors = get_neighbors(grid, pos)
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
    return []

def print_path(grid, path):
    grid_copy = [line.copy() for line in grid]
    for pos in path[:10]:
        i, j = pos
        grid_copy[i][j] = 'X'
        for line in grid_copy:
            print(''.join(line))
    
def print_cheat(grid, first, second):
    grid_copy = [line.copy() for line in grid]
    grid_copy[first[0]][first[1]] = '1'
    grid_copy[second[0]][second[1]] = '2'
    for line in grid_copy:
        print(''.join(line))

def get_cheats(path,grid):
    cheats = {}
    for i in range(len(path)):
        for j in range(i,len(path)):
            if (path[i][0] == path[j][0] and abs(path[i][1]-path[j][1]) == 2 and grid[path[i][0]][(path[i][1]+path[j][1])//2] == '#') or (path[i][1] == path[j][1] and abs(path[i][0]-path[j][0]) == 2 and grid[(path[i][0]+path[j][0])//2][path[i][1]] == '#'):
                savedTime = j - i - 2
                if savedTime not in cheats:
                    cheats[savedTime] = 1
                else:
                    cheats[savedTime] += 1

    return cheats

path = get_race_track(grid, start, end)
cheats = get_cheats(path,grid)
print(cheats)
count = 0
for key in cheats:
    if key >= 100:
        count += cheats[key]

print(count)