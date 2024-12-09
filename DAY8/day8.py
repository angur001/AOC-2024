

f = open("input.txt", "r")
space =[[elem for elem in line.strip()] for line in f.readlines()]

dictionary = {}
for i in range(0, len(space[0])):
    for j in range(0, len(space)):
        if space[j][i] == ".":
            continue
        if space[j][i] in dictionary:
            dictionary[space[j][i]].append((j, i))
        else:
            dictionary[space[j][i]] = [(j, i)]

anti_nodes = set()

def add_antinodes(arr):
    global anti_nodes
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            d_lines = arr[i][0] - arr[j][0]
            d_colones = arr[i][1] - arr[j][1]
            pos1 = (arr[i][0] + d_lines, arr[i][1] + d_colones)
            pos2 = (arr[j][0] - d_lines, arr[j][1] - d_colones)
            # check if position is in bound
            if not(pos1[0] < 0 or pos1[0] >= len(space) or pos1[1] < 0 or pos1[1] >= len(space[0])):
                print(f"added {pos1}")
                anti_nodes.add(pos1)

            if not(pos2[0] < 0 or pos2[0] >= len(space) or pos2[1] < 0 or pos2[1] >= len(space[0])):
                print(f"added {pos2}")
                anti_nodes.add(pos2)


for frequencies in dictionary.values():
    print(frequencies)
    add_antinodes(frequencies)

print(len(anti_nodes))
