def isValidLevel(arr):
    isIncreasing = (arr[1] > arr[0])
    for i in range(len(arr)-1):
        if (0 < abs(arr[i+1] - arr[i]) <= 3 and not( (arr[i+1] > arr[i]) ^ isIncreasing )):
            continue
        else:
            return False
    return True

def IsValidLevelWithErrorForce(arr):
    for i in range(len(arr)):
        if (isValidLevel(arr[:i] + arr[i+1:])):
            return True
    return False


f = open("input.txt", "r")
sum = 0
for line in f:
    level = line.strip().split(" ")
    level = [int(x) for x in level]
    if (isValidLevel(level) or IsValidLevelWithErrorForce(level)):
        sum += 1

print(sum)
