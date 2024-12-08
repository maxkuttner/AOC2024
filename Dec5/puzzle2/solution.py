from collections import defaultdict, deque


def read_data(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return parse_input(data)


def parse_input(input_data):
    """Parses the input into rules and updates."""
    sections = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in
             sections[0].split("\n")]
    updates = [list(map(int, update.split(","))) for update in
               sections[1].split("\n")]
    return rules, updates


def build_graph(rules):
    """Builds a directed graph from the rules."""
    # {<num>: <set of proceeding numbers of <num>>}
    graph = {}
    for X, Y in rules:
        graph.setdefault(X, set()).add(Y)
    return graph


def is_valid_update(update, graph):
    """Checks if an update respects the ordering rules."""

    seen = set()
    for u in update:
        # if the intersection between the seen ones and the ones that
        # shall proceed the current page u is not empty then we have a
        # violation of the rule
        if graph.get(u, set()) & seen:
            return False
        seen.add(u)
    return True


def reorder_update(update, graph):
    """Reorders an incorrect update to satisfy the graph rules."""
    # Build a subgraph for the pages in the update
    subgraph = {node: set() for node in update}
    for node in update:

        if node in graph:
            # get all relevant proceeding numbers after
            # the number <node> that are relevant for the update
            # e.h. 1: {2,3,4,5} and update = [2,4] -> 1: {2,4}
            subgraph[node] = graph[node] & set(update)

    # Perform topological sort to find a valid order
    try:
        return topological_sort(subgraph, update)
    except ValueError:
        return None  # If the graph has a cycle, return None


def topological_sort(subgraph, pages):
    """Performs topological sort on the subgraph for the given pages."""
    # Calculate in-degrees
    in_degree = {node: 0 for node in pages}
    for node in subgraph:
        # subgraph[node] contains the set of all nodes that the current
        # node points to (its "neighbors").
        for neighbor in subgraph[node]:
            in_degree[neighbor] += 1

    # Collect nodes with no incoming edges
    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_order = []

    while queue:
        # simply append the nodes without any edges to the sorted list
        # we can do this because there are no nodes poiting to it anymore
        current = queue.popleft()
        sorted_order.append(current)

        # Reduce in-degree of neighbors
        # This step reflects that one of the edges pointing to
        # neighbor has been processed
        for neighbor in subgraph.get(current, []):
            in_degree[neighbor] -= 1
            # when there is a node with no incoming nodes, we
            # add it to the list
            if in_degree[neighbor] == 0:
                # add it to the right of the deque as it is next to
                # be processed as a node with no dependencies
                # and therefore can be added to the sorted list
                queue.append(neighbor)

    # ... if the queue is empty
    # Check if we were able to sort all nodes
    if len(sorted_order) == len(pages):
        return sorted_order
    else:
        # i dont think this will happen here but in this case
        # there is no defined way of proceeding
        raise ValueError("The graph contains a cycle, and no valid order exists.")


if __name__ == "__main__":
    rules, updates = read_data('data.txt')
    graph = build_graph(rules)
    middle_num_sum = 0
    for update in updates:
        if not is_valid_update(update, graph):
            sorted = reorder_update(update, graph)
            if sorted:
                middle_num_sum += sorted[len(sorted) // 2]
    print(middle_num_sum)
