import re

import utils
from utils import _print as print

# sample = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
sample = utils.get_aoc_input(3)

print(sample)
pattern = r"mul\(\d*,\d*\)|do\(\)|don't\(\)"
real_data = re.findall(pattern, sample)

print(real_data)


def get_numbers(data: str) -> tuple[int, int]:
    data = data[3:]  # remove 'mul'
    data = data[1:-1]  # remove parenthesis
    a, b = map(int, data.split(","))

    return a, b


# Part 1
total_part_1 = 0
for data in real_data:
    if "do" in data:
        continue
    a, b = get_numbers(data)
    total_part_1 += a * b

utils.answer(1, total_part_1)

# Part 2
total_part_2 = 0
enabled = True
for data in real_data:
    if "don't" in data:
        enabled = False
        continue
    if "do" in data:
        enabled = True
        continue

    if not enabled:
        continue

    a, b = get_numbers(data)
    total_part_2 += a * b

utils.answer(2, total_part_2)
