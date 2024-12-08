def read_data(file_name):
    """Read data from file."""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(list(line.strip()))
    return _data


def count_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Helper function to check boundaries
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    # Helper function to check a diagonal word
    def check_diagonal(x, y, dx, dy, word):
        for i, char in enumerate(word):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != char:
                return False
        return True

    # Iterate over each cell as the center of an X
    for x in range(1, rows - 1):  # Avoid edges
        for y in range(1, cols - 1):  # Avoid edges
            # Check the two diagonals
            top_left_to_bottom_right = check_diagonal(x - 1, y - 1, 1, 1, "MAS")
            bottom_left_to_top_right = check_diagonal(x + 1, y - 1, -1, 1, "MAS")
            top_right_to_bottom_left = check_diagonal(x + 1, y - 1, -1, 1,
                                                      "SAM")
            bottom_right_to_top_left = check_diagonal(x - 1, y - 1, 1, 1,
                                                      "SAM")
            if top_left_to_bottom_right and (bottom_left_to_top_right or
                                             top_right_to_bottom_left):
                count += 1
            elif bottom_left_to_top_right and (top_left_to_bottom_right or
                                               bottom_right_to_top_left):
                count += 1
            elif top_right_to_bottom_left and(top_left_to_bottom_right or
                                              bottom_right_to_top_left):
                count += 1
            elif bottom_right_to_top_left and(bottom_left_to_top_right or
                                              top_right_to_bottom_left):
                count += 1

    return count


if __name__ == '__main__':
    _data = read_data("data.txt")
    print(count_x_mas(_data))
