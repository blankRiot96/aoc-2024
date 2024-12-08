import argparse
import json
import time
import typing as t
from collections.abc import Callable
from dataclasses import dataclass

import click
import clipboard
import colorama
import requests

parser = argparse.ArgumentParser(
    prog="aoc_util",
    description="Contains utilities for AOC",
)

parser.add_argument("-d", "--debug", action="store_true")
args = parser.parse_args()

DEBUGGING: bool = args.debug


@dataclass(unsafe_hash=True)
class Vec2:
    x: int
    y: int


def cprint(text: str, color: str, *args, **kwargs) -> None:
    print(
        getattr(colorama.Fore, color.upper()) + text + colorama.Fore.RESET,
        *args,
        **kwargs,
    )


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
    if DEBUGGING:
        return get_aoc_sample_input(day)

    globals()["print"] = _print
    globals()["rich.print"] = _print
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


def perf(func: Callable):
    start = time.perf_counter()
    func()
    end = time.perf_counter()

    click.echo(f"`{func.__name__}` took {end - start:.2f}s to run")


def answer(part: t.Literal[1, 2], value: int) -> None:
    click.echo(
        f"{colorama.Fore.GREEN}PART {part}{colorama.Fore.RESET} = {colorama.Fore.BLUE}{value}{colorama.Fore.RESET}"
    )
    clipboard.copy(str(value))


if __name__ == "__main__":
    print(get_aoc_input(1))
