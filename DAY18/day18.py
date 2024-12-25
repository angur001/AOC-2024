from heapq import heappop, heappush

data = [(int(x), int(y)) for line in open('input.txt') for x, y in [line.strip().split(',')]]
maxSize = 1024
data = data[:maxSize]
spaceSize = 70 + 1

space = [['.' for _ in range(spaceSize)] for _ in range(spaceSize)]
for x, y in data:
    space[y][x] = '#'

def printSpace():
    for row in space:
        print(''.join(row))
    print()

def getNeighbours(row, col):
    neighbours = []
    # check uo,down,left,right and add to neighbours if valid
    if row - 1 >= 0 and space[row-1][col] != '#':
        neighbours.append((row-1, col))
    if row + 1 < spaceSize and space[row+1][col] != '#':
        neighbours.append((row+1, col))
    if col - 1 >= 0 and space[row][col-1] != '#':
        neighbours.append((row, col-1))
    if col + 1 < spaceSize and space[row][col+1] != '#':
        neighbours.append((row, col+1))
    return neighbours
    

def djiktra(start, end):
    priority_queue = []
    distances = {}

    distances[start] = 0
    heappush(priority_queue, (0,start))

    while priority_queue:   
        cost, pos = heappop(priority_queue)
        if pos == end:
            return cost
        
        neighbors = getNeighbours(pos[0], pos[1])
        for neighbor in neighbors:
            if neighbor in distances:
                if distances[neighbor] > cost + 1:
                    distances[neighbor] = cost + 1
                    heappush(priority_queue, (cost+1, neighbor))
            else:
                distances[neighbor] = cost + 1
                heappush(priority_queue, (cost+1, neighbor))

    return float('inf')

print(djiktra((0,0), (70,70)))

