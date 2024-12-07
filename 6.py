import time
from copy import deepcopy

import colorama
import rich

import utils

# rich.print = utils._print
# print = utils._print
sample = utils.get_aoc_input(6)

# sample = utils.get_aoc_sample_input(6)

room = [list(row) for row in sample.splitlines()]
max_x = len(room[0]) - 1
max_y = len(room) - 1
original_room = deepcopy(room)
downwards = "v"
upwards = "^"
right = ">"
left = "<"


def is_guard_in_row(row: list[str]) -> bool:
    for move in (downwards, upwards, right, left):
        if move in row:
            return True

    return False


for y, row in enumerate(room):
    for move in (downwards, upwards, right, left):
        if move in row:
            guard_pos = [row.index(move), y]

original_guard_pos = guard_pos.copy()


def get_guard_char(guard_pos, room=room):
    return room[guard_pos[1]][guard_pos[0]]


def is_guard_out(guard_pos, room=room):
    exited_down = get_guard_char(guard_pos, room) == downwards and guard_pos[1] == max_y
    exited_up = get_guard_char(guard_pos, room) == upwards and guard_pos[1] == 0
    exited_right = get_guard_char(guard_pos, room) == right and guard_pos[0] == max_x
    exited_left = get_guard_char(guard_pos, room) == left and guard_pos[0] == 0

    return exited_down or exited_up or exited_right or exited_left


# PART 1
prev_guard_pos = guard_pos.copy()
distinct_spots = set()
while not is_guard_out(guard_pos):
    distinct_spots.add(tuple(guard_pos))
    for y, row in enumerate(room):
        if not is_guard_in_row(row):
            continue

        guard_char = get_guard_char(guard_pos)
        x = row.index(guard_char)

        if guard_char == upwards:
            if y == 0:
                break
            if room[y - 1][x] == "#":
                guard_char = right
            else:
                guard_pos[1] -= 1
        elif guard_char == downwards:
            if y == max_y:
                break
            if room[y + 1][x] == "#":
                guard_char = left
            else:
                guard_pos[1] += 1
        elif guard_char == right:
            if x == max_x:
                break
            if room[y][x + 1] == "#":
                guard_char = downwards
            else:
                guard_pos[0] += 1
        elif guard_char == left:
            if x == 0:
                break
            if room[y][x - 1] == "#":
                guard_char = upwards
            else:
                guard_pos[0] -= 1

        break

    room[prev_guard_pos[1]][prev_guard_pos[0]] = "X"
    room[guard_pos[1]][guard_pos[0]] = guard_char
    prev_guard_pos = guard_pos.copy()

distinct_spots.add(tuple(guard_pos))

utils.answer(1, len(distinct_spots))


# PART 2
total_obstructions_possible = 0


def get_step(guard_pos, new_room):
    return (tuple(guard_pos), get_guard_char(guard_pos, new_room))


def sexy_print_room(room, blocker_pos, guard_pos):
    ender = ""
    for y, row in enumerate(room):
        for x, char in enumerate(row):
            if (x, y) == blocker_pos:
                print(f"{colorama.Fore.YELLOW}{char}{colorama.Fore.RESET}", end=ender)
            elif (x, y) == guard_pos:
                print(f"{colorama.Fore.RED}{char}{colorama.Fore.RED}", end=ender)
            elif char == "#":
                print(f"{colorama.Fore.GREEN}{char}{colorama.Fore.RESET}", end=ender)
            else:
                print(char, end=ender)
        print()


guard_pos = original_guard_pos.copy()
# for row_x in range(max_x + 1):
#     for row_y in range(max_y + 1):
for row_x, row_y in distinct_spots:
    if original_room[row_y][row_x] in ("#", upwards, downwards, right, left):
        continue

    new_room = [row.copy() for row in original_room]
    new_room[row_y][row_x] = "#"

    steps = []
    guard_pos = original_guard_pos.copy()
    prev_guard_pos = guard_pos.copy()
    while not is_guard_out(guard_pos, new_room):
        for y, row in enumerate(new_room):
            if not is_guard_in_row(row):
                continue

            guard_char = get_guard_char(guard_pos, new_room)
            x = row.index(guard_char)

            if guard_char == upwards:
                if y == 0:
                    break
                if new_room[y - 1][x] == "#":
                    guard_char = right
                else:
                    guard_pos[1] -= 1
            elif guard_char == downwards:
                if y == max_y:
                    break
                if new_room[y + 1][x] == "#":
                    guard_char = left
                else:
                    guard_pos[1] += 1
            elif guard_char == right:
                if x == max_x:
                    break
                if new_room[y][x + 1] == "#":
                    guard_char = downwards
                else:
                    guard_pos[0] += 1
            elif guard_char == left:
                if x == 0:
                    break
                if new_room[y][x - 1] == "#":
                    guard_char = upwards
                else:
                    guard_pos[0] -= 1

            break

        new_room[prev_guard_pos[1]][prev_guard_pos[0]] = "X"
        new_room[guard_pos[1]][guard_pos[0]] = guard_char
        prev_guard_pos = guard_pos.copy()
        current_step = get_step(guard_pos, new_room)

        if current_step in steps and not is_guard_out(guard_pos, new_room):
            # print()
            # sexy_print_room(new_room, (x, y), tuple(guard_pos))
            total_obstructions_possible += 1
            print(total_obstructions_possible)
            break
        steps.append(current_step)

utils.answer(2, total_obstructions_possible)
