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

files = []
free_space = []
result = createFile(data)

for i in range(len(result)):
    if i%2 == 0:
        files.append(result[i])
    else:
        free_space.append(result[i])

def compressFile(files, free_space):
    for i in range(len(files)-1, -1, -1):
        for j in range(i):
            if free_space[j].count('.') >= len(files[i]):
                id = free_space[j].index('.')
                for k in range(len(files[i])) :
                    free_space[j][k+id] = files[i][k]
                    files[i][k] = '.'
                break

def alternate_join(l1, l2):
    result = []
    for i in range(len(l1)):
        result.append(l1[i])
        if i < len(l2):
            result.append(l2[i])
    return result

def calculateCheckSum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += i * int(compressed[i])
    return sum


compressFile(files, free_space)
# print(f"files: {files}")
# print(f"free_space: {free_space}")
compacted_file = alternate_join(files, free_space)
compacted_file = [item for sublist in compacted_file for item in sublist]
# print(''.join(compacted_file))
print(f"Checksum: {calculateCheckSum(compacted_file)}")