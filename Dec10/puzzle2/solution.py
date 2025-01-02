def read_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(
                list(map(int, line.strip()))
            )
    return data


# up, down, left, right
directions = [(-1,0),(1,0),(0, -1),(0,1)]

def find_paths(pos, data, path, all_paths):
    x, y = pos
    path.append(pos)
    if data[x][y] == 9:
        all_paths.add(str(path))
        return 1

    for d in directions:
        x_new, y_new = x + d[0], y + d[1]
        # Check bounds and strict increment condition
        if (0 <= x_new < len(data) and 0 <= y_new < len(data[0])
                and data[x_new][y_new] == data[x][y] + 1):
                find_paths((x_new, y_new), data, path, all_paths)

    return all_paths



def find_starts(data):
    starts = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
              starts.append((i, j))
    return starts



def solution(data):

    total_score = 0
    starts = find_starts(data)
    for start_pos in starts:
        npaths = find_paths(start_pos, data, [], set())
        total_score += len(npaths)
    return total_score


if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)