from collections import defaultdict, deque


data = []
with open('data.txt') as f:
    for lin in f.readlines():
        data.append(
            tuple(lin.strip().split('-'))
        )



connections = defaultdict(set)

for a, b in data:
    connections[a].add(b)
    connections[b].add(a)


def bron_kerbosch(r, p, x, graph, cliques):
    """Recursive Bron-Kerbosch algorithm to find maximal cliques."""
    if not p and not x:
        cliques.append(r)
        return

    for node in list(p):
        bron_kerbosch(r | {node}, p & graph[node], x & graph[node], graph,
                      cliques)
        p.remove(node)
        x.add(node)


def find_cliques(graph):
    """Finds all maximal cliques in the given graph."""
    cliques = []
    bron_kerbosch(set(), set(graph.keys()), set(), graph, cliques)
    return cliques

cliques = find_cliques(connections)
maxs = (0, cliques[0])
for i, c in enumerate(cliques[1:]):
    if len(c) > len(maxs[1]):
        maxs = i, c
print(*sorted(list(maxs[1])), sep=',')


