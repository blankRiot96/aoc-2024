import rich

import utils

rich.print = utils._print
print = utils._print
sample = utils.get_aoc_sample_input(6)

sample = utils.get_aoc_input(6)

room = [list(row) for row in sample.splitlines()]
max_x = len(room[0]) - 1
max_y = len(room) - 1

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


def get_guard_char(guard_pos):
    return room[guard_pos[1]][guard_pos[0]]


def is_guard_out(guard_pos):
    exited_down = get_guard_char(guard_pos) == downwards and guard_pos[1] == max_y
    exited_up = get_guard_char(guard_pos) == upwards and guard_pos[1] == 0
    exited_right = get_guard_char(guard_pos) == right and guard_pos[0] == max_x
    exited_left = get_guard_char(guard_pos) == left and guard_pos[0] == 0

    print(f"{max_x=}")
    print(f"{guard_pos=}")
    print(f"{exited_down=}")

    print(f"{exited_up=}")
    print(f"{exited_left=}")
    print(f"{exited_right=}")
    return exited_down or exited_up or exited_right or exited_left


prev_guard_pos = guard_pos.copy()
print(guard_pos)
distinct_spots = set()
while not is_guard_out(guard_pos):
    distinct_spots.add(tuple(guard_pos))
    for y, row in enumerate(room):
        if not is_guard_in_row(row):
            continue

        rich.print(room)
        print(guard_pos)
        guard_char = get_guard_char(guard_pos)
        print(guard_char)
        print(row)
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
                print("HUH?")
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
