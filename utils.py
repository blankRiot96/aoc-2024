import json
import typing as t

import clipboard
import colorama
import requests


def get_aoc_sample_input(day: int) -> str:
    with open(f"samples/{day}.txt") as f:
        return f.read()


with open("aoc_headers.json") as f:
    try:
        AOC_HEADERS = json.load(f)
    except FileNotFoundError:
        print(
            "`aoc_headers.json` needs to be created to use this suite. To do so follow "
            "the steps in the README"
        )


def read_aoc_inputs():
    with open("aoc_inputs.json") as f:
        return json.load(f)


def write_aoc_inputs(aoc_inputs: dict[int, str]):
    with open("aoc_inputs.json", "w") as f:
        json.dump(aoc_inputs, f, indent=2)


def get_aoc_input(day: int) -> str:
    day = str(day)
    aoc_inputs = read_aoc_inputs()

    if day in aoc_inputs:
        return aoc_inputs[day]

    response = requests.get(
        f"https://adventofcode.com/2024/day/{day}/input",
        headers=AOC_HEADERS,
    )
    aoc_inputs[day] = response.text
    write_aoc_inputs(aoc_inputs)

    return aoc_inputs[day]


def _print(
    *values: object,
    sep: str | None = " ",
    end: str | None = "\n",
    file=None,
    flush: t.Literal[False] = False,
):

    pass


def answer(part: t.Literal[1, 2], value: int) -> None:
    print(
        f"{colorama.Fore.GREEN}PART {part}{colorama.Fore.RESET} = {colorama.Fore.BLUE}{value}{colorama.Fore.RESET}"
    )
    clipboard.copy(str(value))


if __name__ == "__main__":
    print(get_aoc_input(1))
