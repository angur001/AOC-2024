
from functools import lru_cache

file = open("input.txt", "r").readlines()
stockTowels = file[0].strip().split(", ")
patterns = [line.strip() for line in file[2:]]

@lru_cache(maxsize=None)
def verifyPattern(pattern):
    if pattern == "":
        return True
    for towel in stockTowels:
        # print(f"Pattern: {pattern}, Towel: {towel}")
        if pattern.startswith(towel):
            if verifyPattern(pattern[len(towel):]):
                return True
    return False

counter = 0
for pattern in patterns:
    res = verifyPattern(pattern)
    print(pattern, res)
    if res:
        counter += 1

print(counter)

