import re
from math import prod
SECONDS = 100
NROW = 103
NCOL = 101


def read_data(file_name):
    data = {}
    p = r'p\=(\-*\d+,\-*\d+)\sv\=(\-*\d+,\-*\d+)'
    with open(file_name) as f:
        lines = re.findall(p, f.read())
    id = 0
    for p, v in lines:
        record = {
                'p': tuple(int(x) for x in p.split(',')),
                'v': tuple(int(x) for x in v.split(','))
            }
        data |= {id: record}
        id += 1
    return data


def create_grid(robots):
    grid = [['.'] * NCOL for _ in range(NROW)]
    for _, trait in robots.items():
        c, r = trait['p']
        if grid[r][c] == '.':
            grid[r][c] = 1
        else:
            grid[r][c] += 1
    return grid


def move(robot):
    c, r = robot["p"]
    dc, dr = robot["v"]
    nc = (c + dc) % NCOL
    nr = (r + dr) % NROW
    robot['p'] = (nc, nr)



def solution(robots):
    for _ in range(SECONDS):
        for id, robot in robots.items():
            move(robot)

        print(robots)

    qs = [0] * 4
    for id, robot in robots.items():
        c, r = robot["p"]

        if c < NCOL // 2:
            # q1, q3
            if r < NROW // 2:
                qs[0] += 1
            elif r > NROW // 2:
                qs[2] += 1
        elif c > NCOL // 2:
            # q2, q4
            if r < NROW // 2:
                qs[1] += 1
            elif r > NROW // 2:
                qs[3] += 1

    return prod(qs)



if __name__ == '__main__':
    robots = read_data('data.txt')
    sol = solution(robots)
    print(sol)