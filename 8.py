import itertools
from collections import defaultdict
from dataclasses import dataclass

import rich

import utils
from utils import Vec2, cprint

sample = utils.get_aoc_input(8)
# sample = """
# .....
# ..A..
# .A...
# .....
# """
# sample = sample.strip()


@dataclass
class Antenna:
    char: str
    cell_pos: Vec2


def is_vec_in_bounds(vec: Vec2, grid_size: tuple[int, int]) -> bool:
    return 0 <= vec.x < grid_size[0] and 0 <= vec.y < grid_size[1]


colors = []


def reset_colors():
    global colors
    colors = ["green", "yellow", "red", "blue"]


reset_colors()
chars = {}


def get_color_for_char(char: str) -> str:
    if char in chars:
        return chars[char]
    chars[char] = colors.pop()
    return chars[char]


def print_grid(grid: list[list[str]], antinodes: set[Vec2]):
    if not utils.DEBUGGING:
        return
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if Vec2(x, y) in antinodes:
                if char != ".":
                    cprint(char, "black", end="")
                else:
                    cprint("#", "black", end="")
            elif char != ".":
                cprint(char, get_color_for_char(char), end="")
            else:
                print(char, end="")
        print()


def part_1():
    unique_chars = set(sample)
    unique_chars.remove("\n")
    unique_chars.remove(".")
    grid = [list(row) for row in sample.splitlines()]
    grid_size = (len(grid[0]), len(grid))

    antenna_map: defaultdict[str, list[Antenna]] = defaultdict(list)

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in unique_chars:
                antenna_map[char].append(Antenna(char=char, cell_pos=Vec2(x, y)))

    antinodes: set[Vec2] = set()
    for char, antennas in antenna_map.items():
        for a1, a2 in itertools.combinations(antennas, 2):
            x_diff = a1.cell_pos.x - a2.cell_pos.x
            y_diff = a1.cell_pos.y - a2.cell_pos.y

            antinode_1_pos = Vec2(
                a2.cell_pos.x + (x_diff * 2), a2.cell_pos.y + (y_diff * 2)
            )
            antinode_2_pos = Vec2(
                a1.cell_pos.x - (x_diff * 2), a1.cell_pos.y - (y_diff * 2)
            )

            if is_vec_in_bounds(antinode_1_pos, grid_size):
                antinodes.add(antinode_1_pos)
            if is_vec_in_bounds(antinode_2_pos, grid_size):
                antinodes.add(antinode_2_pos)

    print_grid(grid, antinodes)
    utils.answer(1, len(antinodes))


def part_2():
    reset_colors()
    unique_chars = set(sample)
    unique_chars.remove("\n")
    unique_chars.remove(".")
    grid = [list(row) for row in sample.splitlines()]
    grid_size = (len(grid[0]), len(grid))

    antenna_map: defaultdict[str, list[Antenna]] = defaultdict(list)

    antinodes: set[Vec2] = set()
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char in unique_chars:
                antenna_map[char].append(Antenna(char=char, cell_pos=Vec2(x, y)))
                antinodes.add(Vec2(x, y))

    for char, antennas in antenna_map.items():
        for a1, a2 in itertools.combinations(antennas, 2):
            x_diff = a1.cell_pos.x - a2.cell_pos.x
            y_diff = a1.cell_pos.y - a2.cell_pos.y

            multiple = 2
            while True:
                antinode_1_pos = Vec2(
                    a2.cell_pos.x + (x_diff * multiple),
                    a2.cell_pos.y + (y_diff * multiple),
                )
                if not is_vec_in_bounds(antinode_1_pos, grid_size):
                    break
                antinodes.add(antinode_1_pos)
                multiple += 1

            multiple_2 = 2
            while True:
                antinode_2_pos = Vec2(
                    a1.cell_pos.x - (x_diff * multiple_2),
                    a1.cell_pos.y - (y_diff * multiple_2),
                )
                if not is_vec_in_bounds(antinode_2_pos, grid_size):
                    break
                antinodes.add(antinode_2_pos)
                multiple_2 += 1

    print_grid(grid, antinodes)
    utils.answer(2, len(antinodes))


if __name__ == "__main__":
    utils.perf(part_1)
    utils.perf(part_2)
