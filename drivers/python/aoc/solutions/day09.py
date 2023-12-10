# project
from aoc.helpers.runnerlib import run_solution


def extrapolate_forward(sequence: list[int]) -> int:
    if all(num == 0 for num in sequence):
        return 0
    
    diffs: list[int] = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i+1] - sequence[i])
    
    inc = extrapolate_forward(diffs)
    return sequence[-1] + inc


def extrapolate_backward(sequence: list[int]) -> int:
    if all(num == 0 for num in sequence):
        return 0
    
    diffs: list[int] = []
    for i in range(len(sequence) - 1):
        diffs.append(sequence[i+1] - sequence[i])
    
    inc = extrapolate_backward(diffs)
    return sequence[0] - inc


def parse_sequence(input: str) -> list[int]:
    return list(map(int, input.split(" ")))


def part1(input: str) -> int:
    sequences = list(map(parse_sequence, input.splitlines()))
    return sum(map(extrapolate_forward, sequences))


def part2(input: str) -> int:
    sequences = list(map(parse_sequence, input.splitlines()))
    return sum(map(extrapolate_backward, sequences))


if __name__ == "__main__":
    run_solution(part1, part2)