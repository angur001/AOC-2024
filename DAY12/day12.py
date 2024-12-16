from time import time as t
from functools import cache


f = open("input.txt", "r")
garden = [[elem for elem in line.strip()] for line in f]


def get_region(pos):
    visited = [pos]
    def aux(pos):
        unvisited_neighbors = get_unvisited_neighbors(pos, visited)
        visited.extend(unvisited_neighbors)
        if len(unvisited_neighbors) == 0:
            return
        else:
            for position in unvisited_neighbors:
                aux(position) 
    aux(pos)
    return set(visited)

def calculate_area(region):
    return len(region)

def get_unvisited_neighbors(pos, s):
    up = (pos[0] - 1, pos[1]) if pos[0] - 1 >= 0 and garden[pos[0] - 1][pos[1]] == garden[pos[0]][pos[1]] else ()
    down = (pos[0] + 1 ,pos[1]) if pos[0] + 1 < len(garden) and garden[pos[0] + 1][pos[1]] == garden[pos[0]][pos[1]] else ()
    left = (pos[0], pos[1] - 1) if pos[1] - 1 >= 0 and garden[pos[0]][pos[1] - 1] == garden[pos[0]][pos[1]] else ()
    right = (pos[0], pos[1] + 1) if pos[1] + 1 < len(garden[pos[0]]) and garden[pos[0]][pos[1] + 1] == garden[pos[0]][pos[1]] else ()
    neighbors = [up, down, left, right]
    return [neighbor for neighbor in neighbors if (neighbor not in s and neighbor != ())]

def calculate_perimeter(region):
    perim = 0
    for position in region:
        up = 0 if (position[0] - 1, position[1]) in region else 1
        down = 0 if (position[0] + 1 ,position[1]) in region else 1
        left = 0 if (position[0], position[1] - 1) in region else 1
        right = 0 if (position[0], position[1] + 1) in region else 1
        perim += up + down + left + right
    return perim


start = t()
visited_plots = set()
total = 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if (i,j) not in visited_plots:
            region = get_region((i,j))
            visited_plots.update(region)
            bulk_perim = calculate_perimeter(region)
            area = calculate_area(region)
            total += bulk_perim*area

end = t()
print(f"total time is {end-start}")
print(total)

