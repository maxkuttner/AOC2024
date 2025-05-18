


file = open("data.txt")

# these wire values we already know
known = {}

# formulas which ought to be applied to the wires
formulas = {}


for line in file:
    if line.isspace(): break
    x, y = line.strip().split(":")
    known[x] = int(y)
    print(line)


for line in file:
    x, op, y, z = line.replace(" -> ", " ").strip().split()
    formulas[z] = (op, x, y)


operators = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y,
}

def calc(wire):
    """
    Look at a wire and its operation - if we know the value of the wire already
    return o.w. see what the value of the connecting wires are
    :param wire:
    :return:
    """
    if wire in known: return known[wire]
    op, x, y = formulas[wire]
    known[wire] = operators[op](calc(x), calc(y))
    return known[wire]

z = []
i = 0
while True:
    k = "z" + str(i).rjust(2, "0")
    if k not in formulas: break
    z.append(calc(k))
    i += 1

print(int("".join(map(str, z[::-1])), 2))