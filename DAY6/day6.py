f = open("input.txt", "r")
data = [[(elem) for elem in line.strip()] for line in f.readlines()]
isVisited = [[False for i in range(len(data[0]))] for j in range(len(data))]
f.close()

# Directions
directions = ["up", "right", "down", "left"]
current_direction = directions[0] # start going up 

# pos = [6, 4]
pos = [37, 65]
data[pos[0]][pos[1]] = "."
isVisited[pos[0]][pos[1]] = True

def advance_guard():
    global pos, current_direction
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
    elif data[new_pos[0]][new_pos[1]] == ".":
        pos = [new_pos[0], new_pos[1]]
        isVisited[pos[0]][pos[1]] = True
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

print(sum([sum([1 for elem in row if elem == True]) for row in isVisited]))
    
