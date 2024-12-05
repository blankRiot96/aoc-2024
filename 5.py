import rich

import utils

sample = utils.get_aoc_input(5)

rules, page_nos = sample.split("\n\n")

rules = rules.splitlines()
page_nos = page_nos.splitlines()

page_nos = [list(map(int, row.split(","))) for row in page_nos]

rules = [list(map(int, row.split("|"))) for row in rules]

total = 0
for row in page_nos:
    for rule in rules:
        before, after = rule
        found_before = False
        found_after = False
        wrong = False
        for page_no in row:
            if page_no == before:
                if found_after:
                    wrong = True
                    break
                found_before = True
            elif page_no == after:
                found_after = True
        if wrong:
            break
    else:
        total += row[int(len(row) / 2)]

print(total)
