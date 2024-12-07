import operator
import time
import typing as t
from collections.abc import Callable
from itertools import product

import rich

import utils

sample = utils.get_aoc_input(7)


def is_test_achievable(
    test_value: int, numbers: list[int], operators: list[Callable]
) -> bool:
    for operator_sequence in product(operators, repeat=len(numbers) - 1):
        result = numbers[0]
        operator_sequence = iter(operator_sequence)
        for number in numbers[1:]:
            current_operator = next(operator_sequence)
            result = current_operator(result, number)

        if result == test_value:
            return True

    return False


def part_1():
    rows = [row.split(":") for row in sample.splitlines()]
    calibrations = {int(row[0]): list(map(int, row[1].split())) for row in rows}

    operators = [operator.add, operator.mul]

    calibration_sum = sum(
        test_value
        for test_value, numbers in calibrations.items()
        if is_test_achievable(test_value, numbers, operators)
    )

    utils.answer(1, calibration_sum)


def part_2():
    rows = [row.split(":") for row in sample.splitlines()]
    calibrations = {int(row[0]): list(map(int, row[1].split())) for row in rows}

    concat = lambda a, b: int(f"{a}{b}")
    operators = [operator.add, operator.mul, concat]

    calibration_sum = sum(
        test_value
        for test_value, numbers in calibrations.items()
        if is_test_achievable(test_value, numbers, operators)
    )

    utils.answer(2, calibration_sum)


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)
