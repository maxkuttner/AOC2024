from collections import defaultdict, deque

def read_data(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(list(line.strip()))
    return data

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def solution(data):
    nrows = len(data)
    ncols = len(data[0])
    letters = defaultdict(set)
    for i in range(nrows):
        for j in range(ncols):
            v = data[i][j]
            letters[v].add((i, j))

    # Collect clusters
    clusters = []

    for letter, positions in letters.items():
        visited = set()
        for pos in positions:
            if pos not in visited:
                queue = deque([pos])
                cluster = set()

                while queue:
                    current = queue.pop()
                    cluster.add(current)
                    visited.add(current)

                    for dx, dy in directions:
                        new_pos = (current[0] + dx, current[1] + dy)
                        if (0 <= new_pos[0] < nrows and 0 <= new_pos[1] < ncols
                                and new_pos in positions
                                and new_pos not in visited):
                            visited.add(new_pos)
                            queue.append(new_pos)

                clusters.append(cluster)

    # Compute total price
    total_price = 0

    for cluster in clusters:
        cluster_set = set(cluster)
        area = len(cluster)
        perimeter = 0

        for cell in cluster:
            for dx, dy in directions:
                neighbor = (cell[0] + dx, cell[1] + dy)
                if neighbor not in cluster_set:
                    perimeter += 1

        price = area * perimeter
        total_price += price

    return total_price

if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)
