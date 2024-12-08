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


if __name__ == "__main__":
    rules, updates = read_data('data.txt')
    graph = build_graph(rules)
    middle_num_sum = 0
    for update in updates:
        if is_valid_update(update, graph):
            middle_num_sum += update[len(update) // 2]
    print(middle_num_sum)