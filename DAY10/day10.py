f = open("input.txt", "r")
data = [[elem for elem in line.strip()] for line in f]
f.close()

def findTrailHeads(data):
    trailHeads = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "0":
                trailHeads.append((i, j))
    return trailHeads

TrailHeads = findTrailHeads(data)

def calculateTrailHeadScore(TrailHead):
    reachedNines = []
    def aux(height, pos):
        if int(data[pos[0]][pos[1]]) != height:
            return 0
        elif int(data[pos[0]][pos[1]]) == height == 9:
            if pos not in reachedNines:
                reachedNines.append(pos)
                return 1
            return 0
        else:
            up = (pos[0] - 1, pos[1]) if pos[0] - 1 >= 0 else pos
            down = (pos[0] + 1, pos[1]) if pos[0] + 1 < len(data) else pos
            left = (pos[0], pos[1] - 1) if pos[1] - 1 >= 0 else pos
            right = (pos[0], pos[1] + 1) if pos[1] + 1 < len(data[pos[0]]) else pos
            return aux(height + 1, up) + aux(height + 1, down) + aux(height + 1, left) + aux(height + 1, right)
    return aux(0, TrailHead)

score = 0
for trailHead in TrailHeads:
    score += calculateTrailHeadScore(trailHead)


print(f"first trail head score: {calculateTrailHeadScore(TrailHeads[0])}")
print(TrailHeads)
print(score)
            