f = open("input.txt", "r")
data = f.readlines()[0].strip()
f.close()

def createFile(line):
    result = []
    counter = 0
    for i in range(0, len(line)):
        if i%2 == 0:
            txt = []
            for j in range(0, int(line[i])):
                txt.append(str(counter))
            result.append(txt)
            counter += 1
        else:
            txt = []
            for j in range(0, int(line[i])):
                txt.append('.')
            result.append(txt)
            
    return result

def compressFile(file):
    right = len(file)-1
    left = 0
    while left < right:
        if file[right] != '.':
            while file[left] != '.':
                left += 1
                if left == right:
                    return file
            file[left] = file[right]
            file[right] = '.'
        right -= 1

    return file

def calculateCheckSum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += i * int(compressed[i])
    return sum

# print(data)
result = createFile(data)
result = [item for sublist in result for item in sublist]
# print("".join(result))
compressed = compressFile(result)
# print("".join(compressed))
print(calculateCheckSum(compressed))
