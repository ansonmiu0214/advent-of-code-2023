# built-ins
from collections import defaultdict
from typing import NamedTuple

# project
from aoc.helpers.runnerlib import run_solution


Position = tuple[int, int]
SchematicGrid = list[list[str]]


class SchematicNumber(NamedTuple):
    value: int
    start_pos: Position
    end_pos: Position


def load_schematic(input: str) -> SchematicGrid:
    return [list(line) for line in input.splitlines()]


def parse_schematic_numbers(schematic: SchematicGrid):
    for row_idx, row in enumerate(schematic):
        start_col_idx = 0
        while start_col_idx < len(row):
            number = 0
            end_col_idx = start_col_idx
            while end_col_idx < len(row) and row[end_col_idx].isdigit():
                number *= 10
                number += int(row[end_col_idx])
                end_col_idx += 1
            
            if number == 0:
                start_col_idx = end_col_idx + 1
            else:
                start_pos = (row_idx, start_col_idx)
                end_pos = (row_idx, end_col_idx - 1)
                yield SchematicNumber(number, start_pos, end_pos)

                start_col_idx = end_col_idx


def is_symbol(cell: str) -> bool:
    return not cell.isdigit() and cell != "."


def find_adjacent_symbols(schematic: SchematicGrid, start_pos: Position, end_pos: Position) -> list[tuple[str, Position]]:
    num_rows, num_cols = len(schematic), len(schematic[0])
    start_pos_row, start_pos_col = start_pos
    end_pos_row, end_pos_col = end_pos

    adjacent_symbols: list[tuple[str, Position]] = []
    for row in range(start_pos_row - 1, end_pos_row + 2):
        for col in range(start_pos_col - 1, end_pos_col + 2):
            if not (0 <= row < num_rows and 0 <= col < num_cols):
                continue

            if is_symbol(schematic[row][col]):
                adjacent_symbols.append((schematic[row][col], (row, col)))

    return adjacent_symbols


def has_adjacent_symbol(schematic: SchematicGrid, start_pos: Position, end_pos: Position) -> bool:
    return bool(find_adjacent_symbols(schematic, start_pos, end_pos))


def part1(input: str) -> int:
    schematic = load_schematic(input)

    part_numbers: list[int] = []
    for schematic_number in parse_schematic_numbers(schematic):
        if has_adjacent_symbol(schematic, schematic_number.start_pos, schematic_number.end_pos):
            part_numbers.append(schematic_number.value)

    return sum(part_numbers)


def part2(input: list[str]) -> int:
    schematic = load_schematic(input)

    gear_symbol_position_to_part_numbers: dict[Position, list[SchematicNumber]] = defaultdict(list)
    for schematic_number in parse_schematic_numbers(schematic):
        adjacent_symbols = find_adjacent_symbols(schematic, schematic_number.start_pos, schematic_number.end_pos)
        for symbol, (row, col) in adjacent_symbols:
            if symbol == "*":
                gear_symbol_position_to_part_numbers[(row, col)].append(schematic_number)

    gear_ratios: list[int] = []
    for part_numbers in gear_symbol_position_to_part_numbers.values():
        if len(part_numbers) == 2:
            gear_ratios.append(part_numbers[0].value * part_numbers[1].value)

    return sum(gear_ratios)


if __name__ == "__main__":
    run_solution(part1, part2)