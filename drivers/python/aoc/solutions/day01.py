# built-ins
import functools

# project
from aoc.helpers.runnerlib import run_solution


_SPELLING_TO_INT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_digits(line: str, *, english_aware: bool) -> list[int]:
    digits: list[int] = []
    for idx in range(len(line)):
        if line[idx].isdigit():
            digits.append(int(line[idx]))
        elif english_aware:
            for spelling, number in _SPELLING_TO_INT.items():
                if line[idx:].startswith(spelling):
                    digits.append(number)
                    break
    return digits


def parse_calibration_value(line: str, *, english_aware: bool) -> int:
    digits = parse_digits(line, english_aware=english_aware)
    return (digits[0] * 10) + digits[-1]


def part1(input: str) -> int:
    parse_calibration = functools.partial(parse_calibration_value, english_aware=False)
    return sum(map(parse_calibration, input.splitlines()))


def part2(input: list[str]) -> int:
    parse_calibration = functools.partial(parse_calibration_value, english_aware=True)
    return sum(map(parse_calibration, input.splitlines()))


if __name__ == "__main__":
    run_solution(part1, part2)