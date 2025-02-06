


def step(x):
    x = ((x * 64) ^ x) % 16777216
    x = ((x // 32) ^ x) % 16777216
    x = ((x * 2048) ^ x) % 16777216
    return x


step(123)

res = 0
for line in open('data.txt'):
    num = int(line.strip())
    for _ in range(2000):
        num = step(num)
    res += num
print(res)