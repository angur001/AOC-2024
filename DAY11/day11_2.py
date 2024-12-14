from functools import cache
from time import time as t 

stones = open('input.txt').read().strip().split(' ')
stones = [int(x) for x in stones]

@cache
def get_next_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        num = str(stone)
        return [int(num[:len(num)//2]), int(num[len(num)//2:])]
    else:
        return [stone* 2024]
 
@cache
def get_generated_stones_number(stones ,n):
    if n == 0:
        return len(stones)
    else:
        return sum(get_generated_stones_number(tuple(get_next_stone(stone)), n-1) for stone in stones)
    

start = t()
sum = get_generated_stones_number(tuple(stones), 75)
end = t()
print(f"execution time is : {end-start}")