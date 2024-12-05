import rich

import utils

sample = utils.get_aoc_input(5)

rules, page_nos = sample.split("\n\n")

rules = rules.splitlines()
page_nos = page_nos.splitlines()

page_nos = [list(map(int, row.split(","))) for row in page_nos]

rules = [list(map(int, row.split("|"))) for row in rules]


def is_correct(row: list[int]) -> bool:
    for rule in rules:
        before, after = rule
        found_after = False
        wrong = False
        for page_no in row:
            if page_no == before:
                if found_after:
                    wrong = True
                    break
            elif page_no == after:
                found_after = True
        if wrong:
            break
    else:
        return True

    return False


incorrect = []
# PART 1
total = 0
for row in page_nos:
    if is_correct(row):
        total += row[int(len(row) / 2)]
    else:
        incorrect.append(row)

utils.answer(1, total)


# PART 2
def get_after_indeces(n1, row) -> list[int]:
    after_indeces = []
    for rule in rules:
        if rule[0] == n1:
            try:
                after_index = row.index(rule[1])
                after_indeces.append(after_index)
            except ValueError:
                continue

    return after_indeces


total = 0
for row in incorrect:
    while not is_correct(row):
        for i, n1 in enumerate(row):
            after_indeces = get_after_indeces(n1, row)
            after_indeces.sort()
            if not after_indeces:
                continue
            if i > after_indeces[0]:
                row.remove(n1)
                row.insert(after_indeces[0], n1)
                break

    total += row[int(len(row) / 2)]

utils.answer(2, total)
