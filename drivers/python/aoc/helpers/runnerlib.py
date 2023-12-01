# built-ins
import argparse
import time
from pathlib import Path
from typing import Protocol


class CommandLineArgs(Protocol):
    day: str
    part: 1 | 2
    input_type: str


class Formatter[T](Protocol):
    def __call__(self, value: T) -> str: ...


class Solution[T](Protocol):
    def __call__(self, input: str) -> T: ...


def run_solution[T](
    part1: Solution[T],
    part2: Solution[T],
    *,
    formatter: Formatter[T] = str
) -> None:
    prog = argparse.ArgumentParser()
    prog.add_argument("--day", type=str, required=True)
    prog.add_argument("--part", type=int, choices=[1, 2], required=True)
    prog.add_argument("--input-type", type=str, required=True)

    args: CommandLineArgs = prog.parse_args()

    input_file = (Path("/data") / args.day / args.input_type).with_suffix(".in")
    input = input_file.read_text()
    run_solution = part1 if args.part == 1 else part2

    start_time_in_seconds = time.perf_counter()
    answer = run_solution(input)
    end_time_in_seconds = time.perf_counter()

    elapsed_time = end_time_in_seconds - start_time_in_seconds
    print(
        f"Answer for {args.day} part{args.part} "
        f"using {args.input_type} input: {formatter(answer)}"
    )