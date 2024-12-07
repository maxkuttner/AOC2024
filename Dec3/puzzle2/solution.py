
import re

def regex_solution(file_name):
    """Read data from file"""
    total = 0
    enabled = True
    with open(file_name, "r") as file:
        for line in file:
            for match in re.finditer(
                    r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)",
                    line,
            ):
                instruction = match.group(0)
                if instruction == "do()":
                    enabled = True
                elif instruction == "don't()":
                    enabled = False
                elif instruction.startswith("mul(") and enabled:
                    x, y = map(int, match.groups())
                    total += x * y
    return total


if __name__ == "__main__":
    total = regex_solution("data.txt")
    print(f"Result: {total}")




