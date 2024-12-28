import itertools

def read_data(filename=''):
    data = []
    with open(filename) as file:
        for line in file:
            res, numbers_str = line.split(':')
            data.append((int(res), numbers_str.strip().split(' ')))
    return data


# had to scrap eval as it was not efficient enough
# (besides being highly unsafe)
def evaluate_expression(numbers, operators):
    # Evaluate the expression left to right
    result = int(numbers[0])
    for i in range(1, len(numbers)):
        num = int(numbers[i])
        op = operators[i - 1]
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result) + str(num))  # Concatenate the numbers
    return result


def solution(data):
    operators = {'+', '*', '||'}
    total = 0

    for res, numbers in data:
        # Generate all possible operator combinations (excluding || if there's only one number)
        op_combinations = itertools.product(operators, repeat=len(numbers) - 1)
        found_valid_expression = False

        for op_combo in op_combinations:
            # THIS PATTERN IS more explicit than just break
            if found_valid_expression:
                break
            # Evaluate the expression using the current operator combination
            result = evaluate_expression(numbers, op_combo)
            if result == res:
                total += res
                found_valid_expression = True

    return total


if __name__ == '__main__':
    res_numbers = read_data('data.txt')
    sol = solution(res_numbers)
    print(sol)
