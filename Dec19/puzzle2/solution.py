def read_data(filename):
    towels = []
    with open(filename) as file:
        combos = file.readline().strip().split(', ')
        _ = file.readline()
        for line in file.readlines():
            towels.append(line.strip())

    return combos, towels


def count_combinations(combos, towel, memo):
    if towel in memo:
        return memo[towel]
    # count valid combs
    n = 0

    # towel = []
    if not towel:
        return 1

    for combo in combos:
       # for each valid start count the combinations of the remaining substring
       if towel.startswith(combo):
           n += count_combinations(combos, towel[len(combo):], memo)

    memo[towel] = n
    return n


def solution(combos, towels):
    memo = {}
    total = 0
    for i, towel in enumerate(towels):
        print(f"{i}/{len(towels)}")
        total += count_combinations(combos, towel, memo)
    return total


if __name__ == '__main__':
    combos, towels = read_data('data.txt')
    sol = solution(combos, towels)
    print(sol)
