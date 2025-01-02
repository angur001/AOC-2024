data = open('input.txt').read().split('\n\n')

def getheights(elem):
    height = []
    for i in range(len(elem[0])):
        count = 0
        for j in range(len(elem)):
            if elem[j][i] == "#":
                count += 1
        height.append(count-1)
    return height

keys = []
locks = []
for element in data:
    if element.startswith("#####"):
        locks.append(element.split("\n"))
    elif element.startswith("....."):
        keys.append(element.split("\n"))


good_combinations = 0
for lock in locks:
    lock_heights = getheights(lock)
    for key in keys:
        key_heights = getheights(key)
        if max([sum(x) for x in zip(lock_heights, key_heights)]) <= 5:
            good_combinations += 1

print(good_combinations)

