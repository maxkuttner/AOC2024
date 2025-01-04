from collections import defaultdict, deque

def read_data(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            data.append(list(line.strip()))
    return data

# no need to check all diagonal ones
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_names = ['up', 'down', 'left', 'right']
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

    # Calculate total price
    total_price = 0

    for cluster in clusters:
        cluster_set = set(cluster)
        area = len(cluster)
        nsides = sides(cluster)
        print(f'{area} * { nsides}')
        price = area * nsides
        total_price += price

    return total_price


def sides(cluster):
    # {locale of edge: direction of edge}
    edges = {}
    for x, y in cluster:
        for dir_, edge_type in zip(directions, direction_names):
            dx, dy = dir_
            x_new, y_new = x + dx, y + dy
            if (x_new, y_new) in cluster:
                continue

            # create an edge in the middle of the two points
            x_edge, y_edge = (x + x_new) / 2, (y + y_new) / 2
            # calculate the direction that the edge is facing wrt. the original point in the cartesian plane
            edges[(x_edge, y_edge)] = edge_type

    # ... iterate over all edges - see which ones have the same direction type and exclude the ones to be checked
    visited = set()
    nsides = 0
    for edge, type in edges.items():
        if edge in visited:
            continue
        nsides += 1
        e_x, e_y = edge
        visited.add(edge)
        if e_x % 1 == 0:
            for dr in [-1 ,1]:
                tmp_x = e_x + dr
                while edges.get((tmp_x, e_y)) == type:
                    visited.add((tmp_x, e_y))
                    tmp_x += dr
        else:
            for dr in [-1 ,1]:
                tmp_y = e_y + dr
                while edges.get((e_x, tmp_y)) == type:
                    visited.add((e_x, tmp_y))
                    tmp_y += dr
    return nsides


if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)
