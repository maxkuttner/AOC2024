def read_data(filename=''):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(list(line.strip()))
    return data


def single_solution(grid) -> bool:

    # up, right, down, left
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    gx, gy = -1, -1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                # guard initial position
                gx, gy = i, j

    nrows, ncols = len(grid), len(grid[0])

    visited = set()
    visited.add((gx, gy))

    # initial direction
    dir_ix = 0
    dx, dy = dirs[dir_ix]

    iter = 0
    while True:
        iter += 1
        # check for a cycle
        if iter >= 100000:
            return True

        # Check the position in front of the guard
        nx, ny = gx + dx, gy + dy

        if (not 0 <= nx < nrows) or (not 0 <= ny < ncols):
            # out of bounds
            return False

        if grid[nx][ny] == '#':
            # Obstacle ahead; turn right
            dir_ix = (dir_ix + 1) % 4
            dx, dy = dirs[dir_ix]
        else:
            # Move forward
            visited.add((nx, ny))
            gx, gy = nx, ny


def global_solution():
    grid = read_data('data.txt')
    nrows, ncols = len(grid), len(grid[0])

    count = 0
    for i in range(nrows):
        print('row', i)
        for j in range(ncols):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                if single_solution(grid=grid):
                    count += 1
                grid[i][j] = '.'
    print(count)



if __name__ == '__main__':
    # it is a bruteforce search - it is not pretty
    global_solution()
