# built-ins
from typing import NamedTuple

# project
from aoc.helpers.runnerlib import run_solution


class CubeCounts(NamedTuple):
    red: int = 0
    green: int = 0
    blue: int = 0

    @classmethod
    def from_record(cls, record: str) -> "CubeCounts":
        color_to_count: dict[str, int] = {}

        for cube_groups in record.split(","):
            count, color = cube_groups.strip().split(" ")
            color_to_count[color.strip()] = int(count)
        
        return CubeCounts(**color_to_count)

    @property
    def power(self) -> int:
        return self.red * self.green * self.blue


class GameRecord(NamedTuple):
    id: int
    records: list[CubeCounts]

    @classmethod
    def from_line(cls, line: str) -> "GameRecord":
        game_id, cube_counts = line.split(":")
        parsed_id = int(game_id.removeprefix("Game").strip())
        parsed_cube_counts = [
            CubeCounts.from_record(record.strip())
            for record in cube_counts.split(";")
        ]
        return GameRecord(parsed_id, parsed_cube_counts)


def has_possible_configuration(
    game: GameRecord,
    *,
    max_num_red: int,
    max_num_green: int,
    max_num_blue: int
) -> bool:
    for record in game.records:
        if any([
            record.red > max_num_red,
            record.green > max_num_green,
            record.blue > max_num_blue,
        ]):
            return False

    return True


def minimum_possible_cube_counts(game: GameRecord) -> CubeCounts:
    min_num_red = 0
    min_num_green = 0
    min_num_blue = 0

    for record in game.records:
        min_num_red = max(min_num_red, record.red)
        min_num_green = max(min_num_green, record.green)
        min_num_blue = max(min_num_blue, record.blue)

    return CubeCounts(min_num_red, min_num_green, min_num_blue)


def part1(input: str) -> int:
    games = map(GameRecord.from_line, input.splitlines())
    return sum(
        game.id
        for game in games
        if has_possible_configuration(
            game,
            max_num_red=12,
            max_num_green=13,
            max_num_blue=14
        )
    )


def part2(input: list[str]) -> int:
    games = map(GameRecord.from_line, input.splitlines())
    return sum(
        cube_count.power
        for cube_count in map(minimum_possible_cube_counts, games)
    )


if __name__ == "__main__":
    run_solution(part1, part2)