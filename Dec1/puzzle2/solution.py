def read_data(file_name):
    """Read data from file"""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(
                tuple(map(int, line.split()))
            )
    return _data


if __name__ == "__main__":
    data = read_data("data.txt")

    n = len(data)
    score = 0
    l1 = [x for x, y in data]
    l2 = [y for x, y in data]

    # create a hash map for the counts in list 2: O(n)
    count = {}
    for i in range(n):
        if l2[i] not in count:
            count[l2[i]] = 1
        else:
            count[l2[i]] += 1
    # multiple count with number in list 1: O(n)
    for i in range(n):
        score += l1[i] * count.get(l1[i], 0)

    print(score)