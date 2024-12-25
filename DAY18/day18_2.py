from heapq import heappop, heappush
from time import time

data = [(int(x), int(y)) for line in open('input.txt') for x, y in [line.strip().split(',')]]
maxSize = 1024
spaceSize = 70 + 1

space = [['.' for _ in range(spaceSize)] for _ in range(spaceSize)]
for x, y in data[:maxSize]:
    space[y][x] = '#'

def setSpace(data):
    _space = [['.' for _ in range(spaceSize)] for _ in range(spaceSize)]
    for x, y in data:
        _space[y][x] = '#'
    return _space

def printSpace():
    for row in space:
        print(''.join(row))
    print()

def getNeighbours(row, col, space):
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
    

def djiktra(start, end , space):
    priority_queue = []
    distances = {}

    distances[start] = 0
    heappush(priority_queue, (0,start))

    while priority_queue:   
        cost, pos = heappop(priority_queue)
        if pos == end:
            return cost
        
        neighbors = getNeighbours(pos[0], pos[1], space)
        for neighbor in neighbors:
            if neighbor in distances:
                if distances[neighbor] > cost + 1:
                    distances[neighbor] = cost + 1
                    heappush(priority_queue, (cost+1, neighbor))
            else:
                distances[neighbor] = cost + 1
                heappush(priority_queue, (cost+1, neighbor))

    return float('inf')


def dichotomoize(start, end):
    lo = maxSize
    hi = len(data)
    while lo < hi:
        mid = (lo + hi) // 2
        mySpace = setSpace(data[maxSize:mid])
        if djiktra(start, end, mySpace) == float('inf'):
            hi = mid
        else:
            lo = mid + 1
    return data[lo-1]

start = time()
result = dichotomoize((0,0), (70,70))
end = time()
print(f"fist byte that will close the path is {result}")
print(f"Time taken is {end-start} seconds")

