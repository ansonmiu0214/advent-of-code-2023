# project
from aoc.helpers.runnerlib import run_solution


def extract_calories(input: str) -> list[int]:
    return [
        sum(int(food.strip()) for food in elf.splitlines())
        for elf in input.split("\n\n")
    ]


def part1(input: str) -> int:
    calories_by_elf = extract_calories(input)
    return max(calories_by_elf)


def part2(input: list[str]) -> int:
    calories_by_elf = extract_calories(input)
    return sum(sorted(calories_by_elf, reverse=True)[:3])


def format_calories(calories: int) -> str:
    return f"{calories:,} calories"


if __name__ == "__main__":
    run_solution(part1, part2, formatter=format_calories)