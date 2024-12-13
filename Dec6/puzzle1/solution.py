def read_data(filename=''):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(list(line.strip()))
    return data


def solution():
    # read data
    grid = read_data('data.txt')

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

    while True:
        # Check the position in front of the guard
        nx, ny = gx + dx, gy + dy

        if (not 0 <= nx < nrows) or (not 0 <= ny < ncols):
            # out of bounds
            break

        if grid[nx][ny] == '#':
            # Obstacle ahead; turn right
            dir_ix = (dir_ix + 1) % 4
            dx, dy = dirs[dir_ix]
        else:
            # Move forward
            visited.add((nx, ny))
            gx, gy = nx, ny

    print(len(visited))


if __name__ == '__main__':
    solution()
