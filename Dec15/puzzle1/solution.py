def read_data(filename):

    grid = []
    steps = ""

    part = 0
    with open(filename) as file:
        for line in file:
            if line.startswith("\n"):
                part += 1
            if part == 0:
               grid.append(list(line.strip()))
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
        objects = []
        cr, cc = r, c
        can_move = True
        while True:
            cr += dr
            cc += dc
            if grid[cr][cc] == '#':
                can_move = False
                break
            if grid[cr][cc] == 'O':
                objects.append((cr, cc))
            if grid[cr][cc] == '.':
                break
        if can_move:
            # move robot
            grid[r][c] = "."
            grid[r + dr][c + dc] = "@"
            r, c = r + dr, c + dc
            # move rest of boxes
            for ob_r, ob_c in objects:
                grid[ob_r + dr][ob_c + dc] = "O"

    for r in grid:
        print(*r)


    return sum(
        [
            100 * x + y
            for x in range(nrows)
            for y in range(ncols) if grid[x][y] == "O"
        ]
    )











if __name__ == "__main__":
    grid, steps = read_data("data.txt")
    sol = solution(grid, steps)
    print(sol)
    # print(data, steps)