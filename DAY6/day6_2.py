f = open("input.txt", "r")
data = [[(elem) for elem in line.strip()] for line in f.readlines()]
isVisited = [[(False, "") for i in range(len(data[0]))] for j in range(len(data))]
f.close()

# Directions
directions = ["up", "right", "down", "left"]
current_direction = directions[0] # start going up 

# pos = [6, 4]
pos = [37, 65]
data[pos[0]][pos[1]] = "."
isVisited[pos[0]][pos[1]] = (True, current_direction)
count = 0

encounteredObstacles = 0
loops = 0

def advance_guard_until_4_walls(pos, current_direction):
    global encounteredObstacles, isVisited
    y , x = pos

    if current_direction == "up":
        new_pos = [y-1, x]
    elif current_direction == "right":
        new_pos = [y, x+1]
    elif current_direction == "down":
        new_pos = [y+1, x]
    elif current_direction == "left":
        new_pos = [y, x-1]

    if new_pos[1] < 0 or new_pos[1] >= len(data[0]) or new_pos[0] < 0 or new_pos[0] >= len(data):
        encounteredObstacles = 500
        return pos, current_direction

    if data[new_pos[0]][new_pos[1]] == ".":
        isVisited[pos[0]][pos[1]] = (True, current_direction)
        return new_pos, current_direction

    elif data[new_pos[0]][new_pos[1]] == "#":
        # if we hit a wall, turn right
        new_direction = directions[(directions.index(current_direction) + 1) % 4]
        encounteredObstacles += 1
        return pos, new_direction

def advance_guard():
    global pos, current_direction, loops, encounteredObstacles, isVisited
    y , x = pos

    if current_direction == "up":
        new_pos = [y-1, x]
    elif current_direction == "right":
        new_pos = [y, x+1]
    elif current_direction == "down":
        new_pos = [y+1, x]
    elif current_direction == "left":
        new_pos = [y, x-1]

    if new_pos[1] < 0 or new_pos[1] >= len(data[0]) or new_pos[0] < 0 or new_pos[0] >= len(data):
        return False

    if data[new_pos[0]][new_pos[1]] == ".":
        # print(f"current pos: {pos}, new pos: {new_pos}")
        inner_pos = [pos[0], pos[1]]
        inner_direction = directions[(directions.index(current_direction) + 1) % 4]
        copy_isVisited = [[elem for elem in row] for row in isVisited]
        data[new_pos[0]][new_pos[1]] = "#"
        prev_encounteredObstacles = encounteredObstacles
        while encounteredObstacles < 208:
            inner_pos, inner_direction = advance_guard_until_4_walls(inner_pos, inner_direction)
            if encounteredObstacles > 3 and prev_encounteredObstacles != encounteredObstacles:
                if isVisited[inner_pos[0]][inner_pos[1]][0] == True and isVisited[inner_pos[0]][inner_pos[1]][1] == inner_direction:
                    loops += 1
                    # print(f"loop detected if obstacle is at {new_pos}")
                    break
                prev_encounteredObstacles = encounteredObstacles
            
        encounteredObstacles = 0
        isVisited = [[elem for elem in row] for row in copy_isVisited]

        data[new_pos[0]][new_pos[1]] = "."
        pos = [new_pos[0], new_pos[1]]
        isVisited[pos[0]][pos[1]] = (True, current_direction)
    elif data[new_pos[0]][new_pos[1]] == "#":
        # if we hit a wall, turn right
        current_direction = directions[(directions.index(current_direction) + 1) % 4]

    return True

def printpos(pos):
    data_copy = [row.copy() for row in data]
    data_copy[pos[0]][pos[1]] = "X"
    for row in data_copy:
        for col in row:
            print(col, end=" ")
        print() 


while advance_guard():
    pass

print(loops)
