from time import time as t


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

def calculate_perimeter_bulk(region):
    return get_up_perimeter(region) + get_down_perimeter(region) + get_right_perimeter(region) + get_left_perimeter(region)
    
def get_up_perimeter(region):
    visited = set()
    perimeter_bulk = 0
    for position in region:
        if position not in visited:
                if (position[0] - 1, position[1]) in region:
                    visited.add(position)
                else:
                    i = 1
                    while (position[0], position[1] - i) in region and (position[0] - 1, position[1] - i) not in region:
                        visited.add((position[0], position[1] - i))
                        i += 1
                    i = 1
                    while (position[0], position[1] + i) in region and (position[0] - 1, position[1] + i) not in region:
                        visited.add((position[0], position[1] + i))
                        i += 1
                    visited.add(position)
                    perimeter_bulk += 1
    return perimeter_bulk


def get_down_perimeter(region):
    visited = set()
    perimeter_bulk = 0
    for position in region:
        if position not in visited:
                if (position[0] + 1, position[1]) in region:
                    visited.add(position)
                else:
                    i = 1
                    while (position[0], position[1] - i) in region and (position[0] + 1, position[1] - i) not in region:
                        visited.add((position[0], position[1] - i))
                        i += 1
                    i = 1
                    while (position[0], position[1] + i) in region and (position[0] + 1, position[1] + i) not in region:
                        visited.add((position[0], position[1] + i))
                        i += 1
                    visited.add(position)
                    perimeter_bulk += 1
    return perimeter_bulk


def get_right_perimeter(region):
    visited = set()
    perimeter_bulk = 0
    for position in region:
        if position not in visited:
                if (position[0], position[1] + 1) in region:
                    visited.add(position)
                else:
                    i = 1
                    while (position[0] - i, position[1]) in region and (position[0] - i, position[1] + 1) not in region:
                        visited.add((position[0] - i, position[1]))
                        i += 1
                    i = 1
                    while (position[0] + i, position[1]) in region and (position[0] + i, position[1] + 1) not in region:
                        visited.add((position[0] + i, position[1]))
                        i += 1
                    visited.add(position)
                    perimeter_bulk += 1
    return perimeter_bulk


def get_left_perimeter(region):
    visited = set()
    perimeter_bulk = 0
    for position in region:
        if position not in visited:
                if (position[0], position[1] - 1) in region:
                    visited.add(position)
                else:
                    i = 1
                    while (position[0] - i, position[1]) in region and (position[0] - i, position[1] - 1) not in region:
                        visited.add((position[0] - i, position[1]))
                        i += 1
                    i = 1
                    while (position[0] + i, position[1]) in region and (position[0] + i, position[1] - 1) not in region:
                        visited.add((position[0] + i, position[1]))
                        i += 1
                    visited.add(position)
                    perimeter_bulk += 1
    return perimeter_bulk
 

start = t()
visited_plots = set()
total = 0
for i in range(len(garden)):
    for j in range(len(garden[0])):
        if (i,j) not in visited_plots:
            region = get_region((i,j))
            visited_plots.update(region)
            bulk_perim = calculate_perimeter_bulk(region)
            area = calculate_area(region)
            total += bulk_perim*area

end = t()
print(f"total time is {end-start}")
print(total)

