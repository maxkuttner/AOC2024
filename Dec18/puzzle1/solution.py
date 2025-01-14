from collections import deque
m = 70
n = 1024


def read_data(filename):
    data = [['.'] * (m + 1) for _ in range(m + 1)]
    hashes = [
        list(map(int, line.split(","))) for line in open(filename)
    ]

    for c, r in hashes[:n]:
        data[r][c] = '#'
    return data


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solution(data):

    q = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while q:
        r, c, steps = q.popleft()
        print(r, c)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr > m or nc > m:
                continue
            if data[nr][nc] == "#":
                continue
            if (nr, nc) in visited:
                continue
            if nr == nc == m:
                return steps + 1

            visited.add((nr, nc))
            q.append((nr, nc, steps + 1))



if __name__ == '__main__':
    data = read_data("data.txt")
    sol = solution(data)
    print(sol)
