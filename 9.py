import itertools

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


def calculate_checksum(data: list[str]) -> int:
    return sum(int(data[i]) * i for i in range(len(data[: data.index(".")])))


def part_1():
    data_types = itertools.cycle(("block", "space"))

    res = ""
    current_digit = 0
    for char in sample:
        dtype = next(data_types)
        if dtype == "block":
            res += str(current_digit) * int(char)
            current_digit += 1
        else:
            res += "." * int(char)

    data = list(res)
    while not is_completed(data):
        digit_index = len(data) - 1
        for e in data[::-1]:
            if e != ".":
                break
            digit_index -= 1

        nearest_dot_index = data.index(".")
        data[nearest_dot_index], data[digit_index] = (
            data[digit_index],
            data[nearest_dot_index],
        )

    utils.answer(1, calculate_checksum(data))


def part_2():
    pass


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)
