
f = open("input.txt", "r")
right_array = []
left_array = []
for line in f:
    r = line.strip().split(" ")[0]
    l = line.strip().split(" ")[3]
    right_array.append(int(r))
    left_array.append(int(l))

right_array.sort()
left_array.sort()
print(zip(right_array, left_array))
result = [abs(i-j) for i,j in zip(right_array, left_array)]
print(sum(result))