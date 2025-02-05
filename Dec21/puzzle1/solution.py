from itertools import permutations, product
num_keypad = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2)
}
arrow_keypad = {
    "^": (0, 1), "A": (0, 2),
    "<": (1, 0), "v": (1, 1), ">": (1, 2)
}
directions = {
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
    "^": (-1, 0)
}


def is_valid_combination(cur_loc, combo, keypad):
    ci, cj = cur_loc
    good = True
    for c in combo[:-1]:
        dr, dc = directions[c]
        ci, cj = ci + dr, cj + dc
        if not (ci, cj) in keypad.values():
            # ... check if out-of-bounds
            good = False
            break
    return good


def ways(code, keypad):
    parts = []
    cur_loc = keypad["A"]

    for c in code:
        next_loc = keypad[c]

        # which direction should we move vertically and horizontally
        drows, dcols = next_loc[0] - cur_loc[0], next_loc[1] - cur_loc[1]

        moves = ""
        if drows > 0:
            moves += "v" * drows
        elif drows < 0:
            moves += "^" * -drows

        if dcols > 0:
            moves += ">" * dcols
        elif dcols < 0:
            moves += "<" * -dcols

        raw_combos = list(set(["".join(x) + "A" for x in permutations(moves)]))
        combos = []
        for combo in raw_combos:
            if is_valid_combination(cur_loc, combo, keypad):
                combos.append(combo)

        parts.append(combos)
        cur_loc = next_loc

    return ["".join(x) for x in product(*parts)]


def get_shortest_sequence(code):
    ways1 = ways(code, num_keypad)
    ways2 = []
    for way in ways1:
        ways2.extend(ways(way, arrow_keypad))
    ways3 = []
    for way in ways2:
        ways3.extend(ways(way, arrow_keypad))

    return min([len(x) for x in ways3])


def solution(data):
    res = 0
    for code in data:
        res += get_shortest_sequence(code) * int(code[:-1])
    return res


if __name__ == "__main__":
    data = open("data.txt").read().strip().split('\n')
    sol = solution(data)
    print(sol)
