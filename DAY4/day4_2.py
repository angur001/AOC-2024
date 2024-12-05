import re

f = open("input.txt", "r")
puzzle = [line.strip() for line in f.readlines()]
pattern = re.compile(r"MAS|SAM")
x_mas_count = 0

for i in range(1,len(puzzle)-1):
    for j in range(1,len(puzzle[0])-1):
        if puzzle[i][j] == 'A':
            str1 = puzzle[i-1][j-1] + puzzle[i][j] + puzzle[i+1][j+1]
            str2 = puzzle[i+1][j-1] + puzzle[i][j] + puzzle[i-1][j+1]
            if pattern.match(str1) and pattern.match(str2):
                x_mas_count += 1

print(x_mas_count)

