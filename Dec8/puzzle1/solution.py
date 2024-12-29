

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
                xprime, yprime = locations[j]
                x_node, y_node = (
                    xprime + (xprime - x),
                    yprime + (yprime - y)
                )
                # check whether the new nodes are in-bounds
                if 0 <= x_node < nrows and 0 <= y_node < ncols:
                    unique_nodes.add((x_node, y_node))
    return len(unique_nodes)











if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)


