data = open('input.txt').read().strip().split('\n')


def generateNextNumber(num):
    res1 = num
    temp = (num * 64)
    res1 = (res1 ^ temp) % 16777216

    res2 = res1
    temp = (res1 // 32)
    res2 = (res2 ^ temp) % 16777216

    res3 = res2
    temp = (res2 * 2048)
    res3 = (res3 ^ temp) % 16777216

    return res3

total = 0
for i in range(0, len(data)):
    num = int(data[i])
    for i in range(2000):
        num = generateNextNumber(num)
    total += num
    
print(total)