from functools import reduce
import sys
from typing import List, Tuple

FILE = sys.argv[1] if len(sys.argv) > 1 else "input.txt"


def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open(FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def calculate_distance(held, remaining):
    return remaining * held





def part_two():
    lines = read_lines_to_list()
    time = int("".join(lines[0].split(":")[1].strip().split()))
    record = int("".join(lines[1].split(":")[1].strip().split()))

    wins = 0
    for i in range(time + 1):
        if calculate_distance(i, time - i) > record:
            wins += 1

    print(f"Part 1: {wins}")



part_two()
