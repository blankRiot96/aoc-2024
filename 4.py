import rich

import utils

sample = utils.get_aoc_input(4)

box = sample.splitlines()
box_width = len(box[0])
box_height = len(box)

SEARCH_WORD = "XMAS"
word_len = len(SEARCH_WORD)


def part_1():
    # Horizontal (and reverse) search
    n_horizontal = 0
    for row in box:
        for i in range(box_width - word_len + 1):
            part = row[i : i + word_len]
            if part == SEARCH_WORD or part[::-1] == SEARCH_WORD:
                n_horizontal += 1

    # Vertical search (and reverse)
    n_vertical = 0
    for col in range(box_width):
        for i in range(box_height - word_len + 1):
            part = "".join(box[i + k][col] for k in range(word_len))
            if part == SEARCH_WORD or part[::-1] == SEARCH_WORD:
                n_vertical += 1

    # Diagonal search (and reverse)
    n_diagonal = 0
    for i in range(box_height):
        for j in range(box_width):
            if i + word_len <= box_height and j + word_len <= box_width:
                part = "".join(box[i + k][j + k] for k in range(word_len))
                if part == SEARCH_WORD or part[::-1] == SEARCH_WORD:
                    n_diagonal += 1
            if i + word_len <= box_height and j - word_len + 1 >= 0:
                part = "".join(box[i + k][j - k] for k in range(word_len))
                if part == SEARCH_WORD or part[::-1] == SEARCH_WORD:
                    n_diagonal += 1

    print(f"{n_horizontal=}")
    print(f"{n_vertical=}")
    print(f"{n_diagonal=}")
    part_1_sum = n_horizontal + n_vertical + n_diagonal
    utils.answer(1, part_1_sum)


def part_2():
    total = 0
    for i in range(1, box_height - 1):
        for j in range(1, box_width - 1):
            char = box[i][j]
            if char == "A":
                res = (
                    box[i - 1][j - 1]
                    + box[i - 1][j + 1]
                    + box[i + 1][j - 1]
                    + box[i + 1][j + 1]
                )

                if res in ("MMSS", "MSMS", "SSMM", "SMSM"):
                    total += 1

    utils.answer(2, total)


if __name__ == "__main__":
    part_2()
