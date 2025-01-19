def read_data(filename):
    towels = []
    with open(filename) as file:
        combos = file.readline().strip().split(', ')
        _ = file.readline()
        for line in file.readlines():
            towels.append(line.strip())

    return combos, towels


def can_form_design(combos, towel):
    n = len(towel)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string can always be formed

    for i in range(1, n + 1):
        for combo in combos:
            if i >= len(combo):
                substr = towel[i - len(combo):i]
                if substr == combo:
                    dp[i] = dp[i] or dp[i - len(combo)]

    return dp[n]


def solution(combos, towels):
    count = 0
    for towel in towels:
        if can_form_design(combos, towel):
            count += 1
    return count


if __name__ == '__main__':
    combos, towels = read_data('data.txt')
    sol = solution(combos, towels)
    print(sol)
