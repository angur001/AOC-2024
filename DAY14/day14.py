f = open("input.txt", "r")
data = f.read().split('\n')
data = [elem.split(" ") for elem in data]
robots = [pair[0].split(",") for pair in data]
speeds = [pair[1].split(",") for pair in data]
for i in range(len(robots)):
    robots[i][0] = int(robots[i][0][2:])
    speeds[i][0] = int(speeds[i][0][2:])
    robots[i][1] = int(robots[i][1])
    speeds[i][1] = int(speeds[i][1])

width = 101
height = 103

def get_next_position(pos, speed):
    pos_x = pos[0] + speed[0]
    pos_y = pos[1] + speed[1]
    if pos_x >= width:
        pos_x = pos_x - width
    if pos_x < 0:
        pos_x = width + pos_x

    if pos_y >= height:
        pos_y = pos_y - height
    if pos_y < 0:
        pos_y = height + pos_y

    return pos_x, pos_y

def get_representation(robots):
    representation = [[0 for i in range(width)] for j in range(height)]
    for position in robots:
        # print(position)
        representation[position[1]][position[0]] += 1
    return representation

def get_safety_factor(representation):
    up_half = representation[:height//2]
    down_half = representation[height//2+1:]
    top_left = [line[:width//2] for line in up_half]
    top_right = [line[width//2+1:] for line in up_half]
    bottom_left = [line[:width//2] for line in down_half]
    bottom_right = [line[width//2+1:] for line in down_half]
    print(f"top_right: {top_right}")
    print(f"top_left: {top_left}")
    print(f"bottom_right: {bottom_right}")
    print(f"bottom_left: {bottom_left}")
    return sum_matrice(top_left) * sum_matrice(top_right) * sum_matrice(bottom_left) * sum_matrice(bottom_right)
    

def sum_matrice(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sum += mat[i][j]
    return sum

def print_representation(representation):
    text = ""
    for i in range(len(representation)):
        for j in range(len(representation[0])):
            if representation[i][j] == 0:
                text = text + '.'
            else:
                text = text + "#"
        text = text + '\n'
    return text


f = open("demo.txt", "a")

for k in range(10000):
    for i in range(len(robots)):
        pos_x, pos_y = get_next_position(robots[i], speeds[i])
        robots[i][0] = pos_x
        robots[i][1] = pos_y
    f.write(print_representation(get_representation(robots)))
    f.write(str(k) + "--------------------------------------------------------------------------------------------------------------------------\n")

    
# print(get_safety_factor(get_representation(robots)))

f.close()

