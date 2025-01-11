import heapq
from collections import defaultdict

INF = float("inf")
def read_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(list(line.strip()))
    return data


class State:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.previous_state = None

    def __hash__(self):
        return hash((self.pos, self.direction))

    def __eq__(self, other):
        if isinstance(other, State):
            return self.pos == other.pos and self.direction == other.direction
        return False

    def __eq__(self, other):
        if isinstance(other, State):
            return self.pos == other.pos and self.direction == other.direction
        return False

    def __lt__(self, other):
        if isinstance(other, State):
            # Compare `pos` first, then `direction`
            return (self.pos, self.direction) < (other.pos, other.direction)
        return NotImplemented

    # Optionally, implement other comparison methods
    def __le__(self, other):
        if isinstance(other, State):
            return (self.pos, self.direction) <= (other.pos, other.direction)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, State):
            return (self.pos, self.direction) > (other.pos, other.direction)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, State):
            return (self.pos, self.direction) >= (other.pos, other.direction)
        return NotImplemented



def solution(data):

    nrows, ncols = len(data), len(data[0])
    pos, end = (0, 0), (0, 0)
    for r in range(nrows):
        for c in range(ncols):
            if data[r][c] == 'S':
                pos = r, c
            if data[r][c] == 'E':
                end = r, c

    # initial dir since raindeer facing east
    initial_dir = (0, 1)
    # (cost, state)
    initial_state = State(pos=pos, direction=initial_dir)
    # create a priority queue
    pq = [(0, initial_state)]
    # tack the minimum cost to get to E
    min_cost = float("inf")
    # track the lowest cost to get to each state
    min_cost_for_state = {initial_state: 0}

    backtrack = defaultdict(set)

    while pq:
        cost, state = heapq.heappop(pq)
        r, c = state.pos
        dr, dc = state.direction

        if cost > min_cost_for_state.get(state, INF):
            # if the cost exceeds the minimum known cost to get to
            # this state - then we do not want to process it
            continue
        min_cost_for_state[state] = cost
        if (r, c) == end:
            # iterate until the costs gets greater than the best one
            if cost > min_cost:
                break
            min_cost = cost

        backtrack[state] = state.previous_state

        possible_moves = [
            (cost + 1, r + dr, c + dc, dr, dc),
            (cost + 1000, r, c, dc, -dr),
            (cost + 1000, r, c, -dc, dr),
        ]

        for ncost, nr, nc, dr, dc in possible_moves:
            if data[nr][nc] == "#":
                continue
            new_state = State(pos=(nr, nc), direction=(dr, dc))
            new_state.previous_state = state
            heapq.heappush(pq, (ncost, new_state))
    print(backtrack)


if __name__ == '__main__':
    data = read_data('data.txt')
    sol = solution(data)
    print(sol)