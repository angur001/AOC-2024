stones = open('input.txt').read().strip().split(' ')
stones = [int(x) for x in stones]



def get_next_stones():
    for i in range(len(stones)):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            num = str(stones[i])
            # print(num)
            stones[i] = int(num[:len(num)//2])
            stones.append(int(num[len(num)//2:]))
        else:
            stones[i] *= 2024
        

for i in range(25):
    # print(stones)
    get_next_stones()


print(len(stones))
            