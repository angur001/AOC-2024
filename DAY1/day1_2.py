
def makeDict(arr):
    d = {}
    for a in arr:
        if a in d.keys():
            d[a] += 1
        else:
            d[a] = 1
    return d

f = open("input.txt", "r")
right_array = []
left_array = []
for line in f:
    r = line.strip().split(" ")[0]
    l = line.strip().split(" ")[3]
    right_array.append(int(r))
    left_array.append(int(l))

left_dict = makeDict(left_array)

sum = 0
for r in right_array:
    if r in left_dict.keys():
        sum += left_dict[r] * r
    
print(sum)