def read_data(file_name):
    """Read data from file"""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(
                list(map(int, line.split()))
            )
    return _data


def is_safe(report):
    """Check if a report is safe."""
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    increasing = all(1 <= d <= 3 for d in diff)
    decreasing = all(-3 <= d <= -1 for d in diff)
    return increasing or decreasing


def count_safe_reports(data):
    """Count the number of safe reports."""
    return sum(1 for report in data if is_safe(report))


if __name__ == "__main__":
    data = read_data("data.txt")
    safe_count = count_safe_reports(data)
    print(f"Number of safe reports: {safe_count}")


