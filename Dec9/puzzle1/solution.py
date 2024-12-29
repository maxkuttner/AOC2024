

def read_data(file_name):
    data = []
    with open(file_name) as f:
        data = map(int, f.readline().strip())
    return list(data)



def solution(data):
    a = []
    id = 0
    for k in range(0, len(data), 2):
        nspaces = data[k+1] if k+1 < len(data) else 0
        a.extend(
            [str(id) for _ in range(data[k])] + ['.' for _ in range(nspaces)]
        )
        id += 1

    right = len(a) - 1
    left = right
    # find the first occurance of empty slot
    for i, el in enumerate(a):
        if el == '.':
            left = i
            break

    while left < len(a) and left < right:

        if a[left] != '.':
            left += 1
            continue
        if a[right] == '.':
            right -= 1
            continue

        # triangle swap
        a[left], a[right] = a[right], a[left]
        right -= 1
        left += 1
        #print(a)
    total_sum = 0

    for i, v in enumerate(a):
        if v == '.':
            break
        else:
            total_sum += int(v) * i
    return total_sum











if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)