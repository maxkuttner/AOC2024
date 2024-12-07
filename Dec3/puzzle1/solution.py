import re

def regex_solution(file_name):
    """Read data from file"""
    total = 0
    with open(file_name, "r") as file:
        for line in file:
            res = re.findall(r'mul\((\d+),(\d+)\)', line)
            total += sum(map(lambda pair: int(pair[0]) * int(pair[1]), res))
    return total


if __name__ == "__main__":
    total = regex_solution("data.txt")
    print(f"Result: {total}")


