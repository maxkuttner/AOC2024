from collections import defaultdict

# Read graph from input file
connections = defaultdict(set)

with open('data.txt') as f:
    for line in f:
        a, b = line.strip().split('-')
        connections[a].add(b)
        connections[b].add(a)

# Find all triangles
triangles = set()

for node in connections:
    neighbors = connections[node]
    for b in neighbors:
        for c in neighbors:
            if b != c and c in connections[b]:  # Check if b and c are connected
                triangle = frozenset([node, b, c])
                triangles.add(triangle)

# Filter triangles where at least one node starts with 't'
triangles_with_t = [t for t in triangles if any(n.startswith('t') for n in t)]

# Print results
print("Total triangles:", len(triangles))
print("Triangles with 't':", len(triangles_with_t))
