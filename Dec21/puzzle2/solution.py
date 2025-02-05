from itertools import permutations, product
from functools import lru_cache


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

@lru_cache(None)
def ways_from_a_to_b(a, b, use_num_keypad):
    kp = num_keypad if use_num_keypad else arrow_keypad
    cur_loc, next_loc = kp[a], kp[b]

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
        if is_valid_combination(cur_loc, combo, kp):
            combos.append(combo)

    return combos

@lru_cache(None)
def get_cost_of_move(a, b, keypad, depth=0):
    if depth == 0:
        return min([len(x) for x in ways_from_a_to_b(a, b, False)])

    ways = ways_from_a_to_b(a, b, keypad)
    best_cost = float("inf")
    for seq in ways:
        seq = "A" + seq
        cost = 0
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i + 1]
            cost += get_cost_of_move(a, b, False, depth - 1)

        best_cost = min(best_cost, cost)

    return best_cost



def cost_of_code(code, depth):
    code = "A" + code
    cost = 0
    for i in range(len(code) - 1):
        a, b = code[i], code[i + 1]
        cost += get_cost_of_move(a, b, True, depth)
        print(cost)
    return cost

def solution(data):
    cost = 0
    for code in data:
        cost += cost_of_code(code, 25) * int(code[:-1])
    return cost

if __name__ == "__main__":
    data = open("data.txt").read().strip().split('\n')
    sol = solution(data)
    print(sol)
