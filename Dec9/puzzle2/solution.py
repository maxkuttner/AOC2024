

def read_data(file_name):
    data = []
    with open(file_name) as f:
        data = map(int, f.readline().strip())
    return list(data)


def solution(data):
    # final array
    a, loc, size, fids = [], [], [], []
    fid = 0
    for k in range(0, len(data), 2):
        # collect location and size of each block
        loc.append(len(a))
        size.append(data[k])
        fids.append(fid)
        # insert filled slots
        a += ([str(fid) for _ in range(data[k])])
        # insert empty slots
        a += (['.' for _ in range(data[k + 1] if k + 1 < len(data) else 0)])
        fid += 1

    for move_id in range(len(fids) - 1, -1, -1):
        # find free space large enough for size[move_id]
        left_free = 0
        size_free = 0
        while left_free < loc[move_id] and size_free < size[move_id]:
            left_free = left_free + size_free
            size_free = 0
            # only search until the block and not beyond
            while a[left_free] != '.':
                left_free += 1
            while left_free + size_free < len(a) and a[left_free + size_free] == '.':
                size_free += 1


        if left_free < loc[move_id] and size_free >= size[move_id]:
            # tri swap
            free_slice = slice(left_free, left_free + size[move_id])
            move_slice = slice(loc[move_id], loc[move_id] + size[move_id])
            a[free_slice] = a[move_slice]
            a[move_slice] = ['.'] * size[move_id]
            #print(a)

    # compute checksum
    return compute_checksum(a)


def find_free_spans_upto(a, fid):
    """Finds contiguous spans of free space (.) in the array."""
    spans = []
    start = None

    for i, block in enumerate(a):
        if block == fid:
            break
        if block == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                spans.append((start, i - start))
                start = None
    return spans


def compute_checksum(a):
    total_sum = 0
    for i, v in enumerate(a):
        if v == '.':
            continue
        else:
            total_sum += int(v) * i

    return total_sum








if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)