import itertools
from itertools import combinations


def read_data(filename=''):
    data = []
    with open(filename) as file:
        for line in file:
            res, numbers_str = line.split(':')
            data.append((res, numbers_str.strip().split(' ')))
    return data

def solution(data):
    operators = {'+', '*'}
    total = 0
    for res, numbers in data:
        op_combinations = itertools.product(operators, repeat=len(numbers) - 1)
        # iterate over all possible combinations of iterator lists
        for op_combo in op_combinations:
            expr = str(numbers[0])
            # add the number and operator to the expression
            for num, op in zip(numbers[1:], op_combo):
                expr += f' {op} {num}'
                expr = str(eval(expr))
            if int(expr) == int(res):
                total += int(res)
                # BREAK here because there can be the same result with different combos
                break

    return total






if __name__ == '__main__':
    res_numbers = read_data('data.txt')
    sol = solution(res_numbers)
    print(sol)