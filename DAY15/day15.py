storeRoom = open("map.txt", "r").read().split("\n")
storeRoom = [[char for char in line] for line in storeRoom]
instructions = open("instructions.txt", "r").read().replace("\n", "")
robot_pos = [24,24]
# robot_pos = [2,2]

def move_guard(pos, symbol):
    new_pos = ()
    match symbol:
        case '^':
            new_pos = (pos[0] - 1, pos[1])
        case 'v':
            new_pos = (pos[0] + 1, pos[1])
        case '>':
            new_pos = (pos[0], pos[1] + 1)
        case "<":
            new_pos = (pos[0], pos[1] - 1)

    if (is_guard_free(pos, symbol)):  
        push_crates(get_crates_to_be_pushed(pos, symbol), symbol)
        storeRoom[pos[0]][pos[1]] = "."
        storeRoom[new_pos[0]][new_pos[1]] = "@"
        robot_pos[0] = new_pos[0]
        robot_pos[1] = new_pos[1]

def is_guard_free(pos, symbol):
    d_row = 0
    d_column = 0
    match symbol:
        case '^':
            d_row = -1
        case 'v':
            d_row = 1
        case '>':
            d_column = 1
        case "<":
            d_column = -1

    check_pos = [pos[0] + d_row, pos[1] + d_column]
    while storeRoom[check_pos[0]][check_pos[1]] != "#":
        if storeRoom[check_pos[0]][check_pos[1]] == '.':
            return True
        elif storeRoom[check_pos[0]][check_pos[1]] == 'O':
            check_pos = [check_pos[0] + d_row, check_pos[1] + d_column]
    return False

def get_crates_to_be_pushed(pos, symbol):
    d_row = 0
    d_column = 0
    crates = []
    match symbol:
        case '^':
            d_row = -1
        case 'v':
            d_row = 1
        case '>':
            d_column = 1
        case "<":
            d_column = -1
    check_pos = [pos[0] + d_row, pos[1] + d_column]
    while storeRoom[check_pos[0]][check_pos[1]] != ".":

        if storeRoom[check_pos[0]][check_pos[1]] == 'O':
            crates.append((check_pos[0], check_pos[1]))
            check_pos = [check_pos[0] + d_row, check_pos[1] + d_column]

    return crates

def push_crates(crates, symbol):
    d_row = 0
    d_column = 0

    if len(crates) == 0:
        return

    match symbol:
        case '^':
            d_row = -1
        case 'v':
            d_row = 1
        case '>':
            d_column = 1
        case "<":
            d_column = -1

    storeRoom[crates[0][0]][crates[0][1]] = "."
    storeRoom[crates[-1][0] + d_row][crates[-1][1] + d_column] = "O"


def printStoreRoom():
    for i in range(len(storeRoom)):
        for j in range(len(storeRoom[0])):
            print(storeRoom[i][j], end='')
        print("")
    print("---------------------------------------------------------------------------------------------------")

def get_score():
    score = 0
    for i in range(len(storeRoom)):
        for j in range(len(storeRoom[0])):
            if storeRoom[i][j] == "O":
                score += i*100 + j
    return score

for instruction in instructions:
    move_guard(robot_pos, instruction)

print(get_score())

