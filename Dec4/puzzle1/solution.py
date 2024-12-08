def read_data(file_name):
    """Read data from file."""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(list(line.strip()))
    return _data


def count_xmas(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    direction_vectors = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, -1),
        (-1, 1)
    ]

    def is_valid(x, y):
        # check that x,y is not out of bounds
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in direction_vectors:
                if check_word(x, y, dx, dy):
                    count += 1
    return count


if __name__ == '__main__':
    _data = read_data("data.txt")
    print(count_xmas(_data, "XMAS"))
