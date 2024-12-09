import itertools
from dataclasses import dataclass

import rich

import utils

sample = utils.get_aoc_input(9)
# sample = "12345"


def is_completed(data: list[str]) -> bool:
    rev = data[::-1]
    found_non = False
    for i, e in enumerate(rev):
        if found_non and e == ".":
            return False
        if e != ".":
            found_non = True

    return True


def calculate_checksum(data: list[int]) -> int:
    total = 0
    current = 0
    for file_id in data:
        total += current * file_id
        current += 1

    return total


def part_1():
    data_types = itertools.cycle(("block", "space"))

    data = []
    current_digit = 0
    for char in sample:
        dtype = next(data_types)
        if dtype == "block":
            data.extend([current_digit] * int(char))
            current_digit += 1
        else:
            data.extend(["."] * int(char))

    print(data)
    data_size = len(data)
    counter = 0
    for i in range(data_size):

        if data[i] == ".":
            if set(data[i:]) == {"."}:
                break
            for j, digit in enumerate(data[::-1]):
                if digit != ".":
                    last_digit_index = data_size - j - 1
                    break
            data[i], data[last_digit_index] = data[last_digit_index], data[i]
            counter += 1

    print(data)
    checksum = calculate_checksum(data[:i])

    utils.answer(1, checksum)


def part_2():
    pass


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)
