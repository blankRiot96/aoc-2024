import itertools

import rich

import utils

# sample = utils.get_aoc_input(9)
sample = "12345"


def transform_input(sample: str) -> tuple[list[list[int]], int]:
    """
    Converts input(122) into [[1, None, None], [2, 2]]
    Where None represents the free space
    """

    result = []
    current = 0
    total_free_space = 0
    print(sample)
    index = 0
    while index < len(sample):
        char = sample[index]
        index += 1
        free_space = None
        if index < len(sample):
            free_space = sample[index]
            free_space = int(free_space)
            index += 1
        digit = int(char)

        row = [current for _ in range(digit)]
        if free_space is not None:
            row.append(free_space)
            total_free_space += free_space

        result.append(row)
        current += 1

    return result, total_free_space


def get_dotted_input(data) -> tuple[str, list[int]]:
    out = ""
    raw = []
    for row in data:
        raw.extend(row[:-1])
        out += "".join(map(str, row[:-1])) + ("." * row[-1])

    return out, raw


def part_1():
    data, free_space = transform_input(sample)

    dotted_input, raw = get_dotted_input(data)
    print(dotted_input)
    dotted_input = list(dotted_input)
    current_dot_index = dotted_input.index(".")

    for travelled_index, digit in enumerate(raw[::-1]):
        dotted_input[current_dot_index] = str(digit)

        try:
            current_dot_index = dotted_input.index(".", current_dot_index + 1)
        except ValueError:
            compressed_files = dotted_input[: travelled_index + free_space + 1]
            break
    else:
        compressed_files = dotted_input[: travelled_index + free_space + 1]

    print("".join(compressed_files))


def part_2():
    pass


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)
