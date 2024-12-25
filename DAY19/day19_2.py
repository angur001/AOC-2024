from functools import lru_cache

file = open("input.txt", "r").readlines()
stockTowels = file[0].strip().split(", ")
patterns = [line.strip() for line in file[2:]]

@lru_cache(maxsize=None)
def verifyPattern(pattern):
    if pattern == "":
        return 1
    count = 0
    for towel in stockTowels:
        if pattern.startswith(towel):
            count += verifyPattern(pattern[len(towel):])
    return count

counter = 0
for pattern in patterns:
    res = verifyPattern(pattern)
    print(pattern, res)
    if res:
        counter += res

print(counter)
