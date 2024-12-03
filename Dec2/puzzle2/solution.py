def read_data(file_name):
    """Read data from file"""
    _data = []
    with open(file_name, "r") as file:
        for line in file:
            _data.append(
                list(map(int, line.split()))
            )
    return _data


def is_safe_with_dampener(report):
    """Check if a report is safe, allowing removal of one level"""
    # Calculate differences between adjacent levels
    diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if already safe
    if all(1 <= d <= 3 for d in diff) or all(-3 <= d <= -1 for d in diff):
        return True

    for i in range(len(report)):
        # Create a new report by removing the i-th level
        reduced_report = report[:i] + report[i + 1:]
        reduced_diff = [
            reduced_report[j + 1] - reduced_report[j]
            for j in range(len(reduced_report) - 1)
        ]
        if (all(1 <= d <= 3 for d in reduced_diff)
                or all(-3 <= d <= -1 for d in reduced_diff)):
            return True

    return False


def count_safe_reports_with_dampener(data):
    """Count the number of safe reports using the Problem Dampener"""
    return sum(1 for report in data if is_safe_with_dampener(report))


if __name__ == "__main__":
    data = read_data("data.txt")
    safe_count = count_safe_reports_with_dampener(data)
    print(f"Number of safe reports: {safe_count}")
