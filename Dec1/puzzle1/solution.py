

def read_data(file_name):
    """Read data from file"""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(
                tuple(map(int, line.split()))
            )
    return _data


if __name__ == '__main__':
    data = read_data("data.txt")

    n = len(data)
    diff = 0
    l1 = [x for x, y in data]
    l2 = [y for x, y in data]

    for i in range(n):
        i_min1 = l1.index(min(l1))
        i_min2 = l2.index(min(l2))
        diff += abs(l1.pop(i_min1) - l2.pop(i_min2))

    print(diff)




