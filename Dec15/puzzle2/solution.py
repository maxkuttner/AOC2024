from collections import deque
from copy import deepcopy


def read_data(filename):

    grid = []
    steps = ""
    replacements = {"#": "##", ".": "..", "@": "@.", "O": "[]"}
    part = 0
    with open(filename) as file:
        for line in file:
            if line.startswith("\n"):
                part += 1
            if part == 0:
               grid.append(
                   list("".join(replacements[x] for x in line.strip()))
               )
            else:
                steps += line.strip()
    return grid, steps


directions = {"v": (1, 0), "^": (-1, 0), ">": (0, 1), "<": (0, -1)}


def solution(grid, steps):
    nrows, ncols = len(grid), len(grid[0])
    # get robot position
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == '@':
                break
        else:
            continue
        break

    for step in steps:
        dr, dc = directions[step]
        objects = [(r, c)]
        can_move = True

        seen = set()
        target_queue = deque(objects)

        while target_queue:
            cr, cc = target_queue.pop()
            cr += dr
            cc += dc
            if (cr, cc) in seen:
                continue
            current_char = grid[cr][cc]
            if current_char == '#':
                can_move = False
                break
            if current_char == '[':
                objs = [(cr, cc), (cr, cc + 1)]
                for ob in objs:
                    if ob not in seen:
                        objects.append(ob)
                        target_queue.append(ob)
                        seen.add(ob)
            if current_char == ']':
                objs = [(cr, cc), (cr, cc - 1)]
                for ob in objs:
                    if ob not in seen:
                        objects.append(ob)
                        target_queue.append(ob)
                        seen.add(ob)
        if can_move:
            # move robot
            copy_grid = deepcopy(grid)

            # move rest of boxes
            for ob_r, ob_c in objects[1:]:
                grid[ob_r][ob_c] = "."
            for ob_r, ob_c in objects[1:]:
                grid[ob_r + dr][ob_c + dc] = copy_grid[ob_r][ob_c]
            grid[r][c] = "."
            grid[r + dr][c + dc] = "@"
            r, c = r + dr, c + dc
    for r in grid:
        print(*r)

    return sum(
        [
            100 * x + y
            for x in range(nrows)
            for y in range(ncols) if grid[x][y] == "["
        ]
    )











if __name__ == "__main__":
    grid, steps = read_data("data.txt")
    for r in grid:
        print(*r)
    sol = solution(grid, steps)
    print(sol)
    # print(data, steps)