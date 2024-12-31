from typing import List, Dict, Tuple
from time import time as t

data = open('input.txt').read().strip().split('\n')
# data = ['1', '2', '3', '2024']
# f = open("part2.txt", "a")


def get_differences(numbers: List[int]) -> List[int]:
    return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

def create_sequence_dictionary(numbers: List[int], sequence_length: int = 4) -> Dict[Tuple[int, ...], int]:
    sequence_dict = {}
    differences = get_differences(numbers)
    
    for i in range(len(differences) - sequence_length + 1):

        diff_sequence = tuple(differences[i:i + sequence_length])
        next_number = numbers[i + sequence_length]
        
        if diff_sequence not in sequence_dict:
            sequence_dict[diff_sequence] = next_number

    
            
    return sequence_dict

def generateNextNumber(num):
    MASK = 0xFFFFFF  # 16777215 (2^24 - 1)
    
    temp = (num << 6) & MASK
    res1 = num ^ temp
    
    temp = res1 >> 5
    res2 = res1 ^ temp
    
    temp = (res2 << 11) & MASK
    res3 = res2 ^ temp
    
    return res3 & MASK

def fillRandomNumbers():
    all_nums = []
    for i in range(len(data)):
        all_nums.append([])
        num = int(data[i])
        all_nums[i].append(num%10)
        for _ in range(2000):
            num = generateNextNumber(num)
            all_nums[i].append(num%10)
    return all_nums

all_nums = fillRandomNumbers()

big_dict = {}
for i in range(len(all_nums)):   
    result = create_sequence_dictionary(all_nums[i])
    # print(all_nums[i])
    # print([all_nums[i][j+1] - all_nums[i][j] for j in range(len(all_nums[i])-1)])
    # print(result)
    # print('-----------------------------------------------------------')

    for key, value in result.items():
        if key in big_dict:
            big_dict[key] += value
        else:
            big_dict[key] = value

    # f.write(f"the max of the big dictioanry after value {i} is {max(big_dict.values())}\n")


top = max(big_dict.values())
print(top)

