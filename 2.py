import rich

import utils
from utils import _print as print

# sample = """
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9
# """

sample = utils.get_aoc_input(2)

reports = sample.splitlines()
reports = list(filter(bool, reports))

reports = [list(map(int, report.split())) for report in reports]


# PART 1


def is_report_safe(report: list[int]) -> bool:
    # All diffs are 1-3
    diffs = [a - b for a, b in zip(report[:-1], report[1:])]
    valid_diffs = all(0 < abs(diff) < 4 for diff in diffs)

    # Increasing or Decreasing
    creasing = sorted(report) == report or sorted(report, reverse=True) == report
    creasing = creasing and (len(set(report)) == len(report))

    return valid_diffs and creasing


n_valid_reports = 0
for report in reports:
    if is_report_safe(report):
        n_valid_reports += 1

utils.answer(1, n_valid_reports)

# PART 2


def is_report_tolerable(report: list[int]) -> bool:
    print(report)
    if not is_report_safe(report):
        for i in range(len(report)):
            report_without_level = report[:i] + report[i + 1 :]
            print(report_without_level)
            if is_report_safe(report_without_level):
                return True

        print("NOT SAFE\n")
        return False

    print("SAFE\n")
    return True


n_safe = 0
for report in reports:
    if is_report_tolerable(report):
        n_safe += 1

utils.answer(2, n_safe)
