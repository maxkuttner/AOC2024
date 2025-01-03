from collections import defaultdict
from functools import reduce

# how often to blink
N_BLINK = 75

def read_data(filename):
    with open(filename) as file:
        data = map(int, file.readline().strip().split(' '))
    return list(data)



def apply_rules(stones: dict):
    new_stones = defaultdict(int)
    for s, count in stones.items():
        if s == 0:
            # O(1)
            new_stones[1] += count
        elif len(str(s)) % 2 == 0:
            stone_str = str(s)
            new_stones[int(stone_str[:len(stone_str)//2])] += count
            new_stones[int(stone_str[len(stone_str)//2:len(stone_str)])] += count
        else:
            #O(1)
            new_stones[s * 2024] += count
    return new_stones


def solution(data):
    stones = defaultdict(int)
    for s in data:
        stones[s] += 1

    for i in range(N_BLINK):
        print(f'{i} / {N_BLINK}')
        stones = apply_rules(stones)

    return sum(stones.values())

if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)
