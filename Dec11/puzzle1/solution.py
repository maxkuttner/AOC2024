from functools import reduce

# how often to blink
N_BLINK = 25

def read_data(filename):
    data = []
    with open(filename) as file:
        data = map(int, file.readline().strip().split(' '))
    return list(data)


def apply_rules(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        stone_str = str(stone)
        _left = [int(stone_str[:len(stone_str)//2])]
        _right = [int(stone_str[len(stone_str)//2:len(stone_str)])]
        return _left + _right
    else:
        return [stone * 2024]


def solution(data):
    for i in range(N_BLINK):
        print(f'{i} / {N_BLINK}')
        data = reduce(lambda x, y: x+y, map(apply_rules, data), [])
    return len(data)

if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)
