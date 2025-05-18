


file = open('data.txt')
locks = []
keys = []
for grid in file.read().split('\n\n'):
    matrix = list(zip(*grid.split("\n")))
    if matrix[0][0] == "#":
        locks.append([col.count("#")-1 for col in matrix])
    else:
        keys.append([col.count("#")-1 for col in matrix])

print(keys)
print(locks)

total = 0
for k in keys:
    for l in locks:
        if all(x + y <= 5 for x, y in zip(k, l)):
            total += 1

print(total)