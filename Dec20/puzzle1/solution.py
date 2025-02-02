from collections import deque

def solution(data):
    nrow, ncol = len(data), len(data[0])
    for i in range(nrow):
        for j in range(ncol):
            if data[i][j] == 'S':
                start = (i, j)
            if data[i][j] == 'E':
                end = (i, j)

    dis = [[-1] * ncol for _ in range(nrow)]
    r, c = start
    dis[r][c] = 0

    while (r, c) != end:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr >= nrow or nc >= ncol:
                continue
            if data[nr][nc] == '#':
                continue
            if dis[nr][nc] != -1:
                continue
            dis[nr][nc] = dis[r][c] + 1
            r, c = nr, nc

    for r in dis:
        print(*r, sep='\t')

    count = 0
    for r in range(nrow):
        for c in range(ncol):
            if data[r][c] == '#': continue
            for dr, dc in [(2, 0), (1, 1), (0, 2), (-1, 1)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= nrow or nc >= ncol: continue
                if data[nr][nc] == '#': continue
                if abs(dis[nr][nc] - dis[r][c]) >= 102:
                    count += 1
    return count


def read_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(list(line.strip()))
    return data




if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)




