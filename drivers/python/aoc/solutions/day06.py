# built-ins
import functools
import operator
import re
from typing import NamedTuple

# project
from aoc.helpers.runnerlib import run_solution


class Race(NamedTuple):
    time: int
    record_distance: int


def num_ways_to_beat_race(race: Race) -> int:
    num_ways = 0

    for time_to_hold in range(race.time + 1):
        time_to_travel = race.time - time_to_hold
        speed = time_to_hold
        distance = speed * time_to_travel
        num_ways += bool(distance > race.record_distance)
    return num_ways


def parse_races(input: str) -> list[Race]:
    times, record_distances = input.splitlines()
    parsed_times = iter(re.split(r"\s+", times))
    parsed_record_distances = iter(re.split(r"\s+", record_distances))

    # skip the '<prefix>:' tokens.
    next(parsed_times)
    next(parsed_record_distances)

    return [
        Race(int(time), int(distance))
        for time, distance in zip(parsed_times, parsed_record_distances)
    ]


def part1(input: str) -> int:
    races = parse_races(input)
    return functools.reduce(operator.mul, map(num_ways_to_beat_race, races), 1)


def combine_races(races: list[Race]) -> Race:
    def join_ints(ints: list[int]) -> int:
        return int("".join(str(int_val) for int_val in ints))

    return Race(
        time=join_ints(map(operator.attrgetter("time"), races)),
        record_distance=join_ints(map(operator.attrgetter("record_distance"), races)),
    )


def part2(input: str) -> int:
    race = combine_races(parse_races(input))
    return num_ways_to_beat_race(race)


if __name__ == "__main__":
    run_solution(part1, part2)