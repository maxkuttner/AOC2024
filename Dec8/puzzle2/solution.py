from ftplib import print_line
from math import gcd

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(list(line.strip()))
    return data


def solution(data):
    nrows = len(data)
    ncols = len(data[0])

    antennas = {}

    # O(n^2)
    for i in range(nrows):
        for j in range(ncols):
            v =  data[i][j]
            if v != '.':
                if v in antennas:
                    antennas[v].append((i, j))
                else:
                    antennas[v] = [(i, j)]


    unique_nodes = set()

    for _, locations in antennas.items():
        n = len(locations)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x, y = locations[i]
                unique_nodes.add((x, y))
                xprime, yprime = locations[j]
                dx, dy = x - xprime, y - yprime
                g = gcd(abs(dx), abs(dy))
                dx //= g
                dy //= g
                x, y = x + dx, y + dy
                while 0 <= x < nrows and 0 <= y < ncols:
                    unique_nodes.add((x, y))
                    x, y = x + dx, y + dy

    return len(unique_nodes)


if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)


