


def step(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x



seq_total = {}

# for each buyer ...
for line in open('data.txt'):
    num = int(line.strip())

    # create a list of prices
    prices = [num % 10]
    for _ in range(2000):
        num = step(num)
        prices.append(num % 10)

    # check all possible 4 long sequences
    visited = set()
    for i in range(len(prices) - 4):
        five_prices = prices[i:i+5]
        diff = tuple([i - j for i, j in zip(five_prices[1:], five_prices[:-1])])
        price_at_end = five_prices[-1]
        # Each buyer only wants to buy one hiding spot
        if diff in visited:
            continue
        visited.add(diff)
        # in the global dict - add to the cumulative bananas
        if diff not in seq_total:
            seq_total[diff] = 0
        seq_total[diff] += price_at_end

print(max(seq_total.values()))

