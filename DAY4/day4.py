import re

pattern = re.compile(r"(?=(XMAS|SAMX))")

def countHorizontally(puzzle):
    return len(pattern.findall(",".join(puzzle)))

def countVertically(puzzle):
    return len(pattern.findall(",".join(["".join(row) for row in zip(*puzzle)])))

def countDiagonally(puzzle):
    diag_1 = []
    diag_2 = []
    for i in range(len(puzzle)):
        diag_1.append("".join([puzzle[j][j+i] for j in range(len(puzzle)-i)]))
        diag_2.append("".join([puzzle[j][len(puzzle)-1-j-i] for j in range(len(puzzle)-i)]))
    for i in range(1, len(puzzle)):
        diag_1.append("".join([puzzle[j+i][j] for j in range(len(puzzle)-i)]))
        diag_2.append("".join([puzzle[j+i][len(puzzle)-1-j] for j in range(len(puzzle)-i)]))
    return len(pattern.findall(",".join(diag_1))) + len(pattern.findall(",".join(diag_2)))
    

f = open("input.txt", "r")
puzzle = [line.strip() for line in f.readlines()]
print(f'Horizontally: {countHorizontally(puzzle)}')
print(f'Vertically: {countVertically(puzzle)}')
print(f'Diagonally: {countDiagonally(puzzle)}')
print(f'Total: {countHorizontally(puzzle) + countVertically(puzzle) + countDiagonally(puzzle)}')