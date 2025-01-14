from collections import deque

m = 70

HASHES = [list(map(int, line.split(","))) for line in open("data.txt")]


def path_exists(n):
    data = [['.'] * (m + 1) for _ in range(m + 1)]

    for c, r in HASHES[:n]:
        data[r][c] = '#'

    q = deque([(0, 0)])
    visited = {(0, 0)}

    while q:
        r, c = q.popleft()

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc

            if nr < 0 or nc < 0 or nr > m or nc > m:
                continue
            if data[nr][nc] == "#":
                continue
            if (nr, nc) in visited:
                continue
            if nr == nc == m:
                return True

            visited.add((nr, nc))
            q.append((nr, nc))

    return False


def solution():
    # print(path_exists(22))
    l = 0
    r = len(HASHES) - 1
    while l < r:
        print(l, r)
        mid = (l + r) // 2
        if path_exists(mid + 1):
            l = mid + 1
        else:
            r = mid
    # l == r
    print(*HASHES[l],l, sep=",")


if __name__ == '__main__':
    sol = solution()
    print(sol)
