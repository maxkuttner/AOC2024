
import re
import numpy as np
from numpy.linalg import det, inv
from Dec12.puzzle1.solution import solution


def read_data(file_name):
    data = []
    ap = r'Button A:\sX\+(\d*),\sY\+(\d*)'
    bp = r'Button B:\sX\+(\d*),\sY\+(\d*)'
    pp = r'Prize:\sX\=(\d*),\sY\=(\d*)'
    tmp = {}
    with open(file_name, 'r') as file:
        for line in file:
            if not line.strip(): continue
            if line[7] == 'A':
                x, y = re.findall(ap, line)[0]
                tmp = {'A': (int(x),int(y))}
            elif line[7] == 'B':
                x, y = re.findall(bp, line)[0]
                tmp |= {'B': (int(x),int(y))}
            elif line[0] == 'P':
                X, Y = re.findall(pp, line)[0]
                tmp |= {'P': (int(X), int(Y))}
                data.append(tmp)
    return data




def solution(data):
    total = 0
    for j, game in enumerate(data):

        xa, ya = game['A']
        xb, yb = game['B']
        X, Y = (i + 10000000000000 for i in game['P'])
        A = np.array([[xa, xb], [ya, yb]])
        z = np.array((X, Y))
        if np.isclose(np.linalg.det(A), 0):  # Ensure matrix is invertible
            continue
        a, b = np.linalg.inv(A) @ z
        # Check positivity and integer closeness
        if a < 0 or b < 0:
            continue

        if round(a) * xa + round(b) * xb == X and round(a) * ya + round(b) * yb == Y:
            print(j)
            print(a, b)
            total += int(round(a)) * 3 + int(round(b)) * 1
    return total





if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)