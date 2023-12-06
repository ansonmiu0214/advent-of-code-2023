# built-ins
import bisect
import math
import operator
from typing import NamedTuple

# project
from aoc.helpers.runnerlib import run_solution


class CategoryEntry(NamedTuple):
    src_start: int
    range_length: int
    dst_start: int

    @classmethod
    def from_string(cls, entry: str) -> "CategoryEntry":
        dst_start, src_start, range_length = list(map(int, entry.split(" ")))
        return CategoryEntry(src_start, range_length, dst_start)

    def in_src_range(self, value: int) -> bool:
        return self.src_start <= value < self.src_start + self.range_length
    
    def get_dst(self, src: int):
        return self.dst_start + (src - self.src_start)
    
    def in_dst_range(self, value: int) -> bool:
        return self.dst_start <= value < self.dst_start + self.range_length
    
    def get_src(self, dst: int):
        return self.src_start + (dst - self.dst_start)

    def __str__(self) -> str:
        return f"[{self.src_start},{self.src_start + self.range_length}) -> {self.dst_start}"


class Almanac(NamedTuple):
    seeds: list[int]
    seed: list[CategoryEntry]
    soil: list[CategoryEntry]
    fertilizer: list[CategoryEntry]
    water: list[CategoryEntry]
    light: list[CategoryEntry]
    temperature: list[CategoryEntry]
    humidity: list[CategoryEntry]


def parse_almanac(input: str, *, reverse_lookup: bool) -> Almanac:
    sections = input.split("\n\n")

    def parse_seeds(section: str):
        return list(map(int, section.removeprefix("seeds: ").split(" ")))

    def parse_map(section: str):
        _category, *entries = section.splitlines()
        parsed_entries: list[CategoryEntry] = []

        for entry in entries:
            parsed_entry = CategoryEntry.from_string(entry)

            if reverse_lookup:
                bisect.insort(parsed_entries, parsed_entry, key=operator.attrgetter("dst_start"))
            else:
                bisect.insort(parsed_entries, parsed_entry, key=operator.attrgetter("src_start"))

        return parsed_entries
    
    attribute_to_parser = [
        ("seeds", parse_seeds),
        ("seed", parse_map),
        ("soil", parse_map),
        ("fertilizer", parse_map),
        ("water", parse_map),
        ("light", parse_map),
        ("temperature", parse_map),
        ("humidity", parse_map),
    ]
    
    parsed_attributes = {
        attribute: parse(section)
        for section, (attribute, parse) in zip(sections, attribute_to_parser)
    }
    return Almanac(**parsed_attributes)


def lookup_destination_for_category(category: list[CategoryEntry], value: int):
    idx = bisect.bisect_left(category, value, key=operator.attrgetter("src_start"))

    try:
        if category[idx].in_src_range(value):
            return category[idx].get_dst(value)
    except IndexError:
        pass

    if idx == 0:
        return value

    prev_category = category[idx - 1]
    if prev_category.in_src_range(value):
        return prev_category.get_dst(value)
    
    return value


def location_for_seed(almanac: Almanac, seed: int):
    ordered_categories = ("seed", "soil", "fertilizer", "water", "light", "temperature", "humidity")
    value = seed
    for category in ordered_categories:
        value = lookup_destination_for_category(getattr(almanac, category), value)
    return value


def lookup_source_for_category(category: list[CategoryEntry], value: int):
    idx = bisect.bisect_left(category, value, key=operator.attrgetter("dst_start"))

    try:
        if category[idx].in_dst_range(value):
            return category[idx].get_src(value)
    except IndexError:
        pass

    if idx == 0:
        return value

    prev_category = category[idx - 1]
    if prev_category.in_dst_range(value):
        return prev_category.get_src(value)
    
    return value


def seed_for_location(almanac: Almanac, location: int):
    ordered_categories = ("seed", "soil", "fertilizer", "water", "light", "temperature", "humidity")
    value = location
    for category in reversed(ordered_categories):
        value = lookup_source_for_category(getattr(almanac, category), value)
    return value


def seed_in_almanac_range(almanac: Almanac, seed: int):
    for idx in range(0, len(almanac.seeds), 2):
        start, length = almanac.seeds[idx], almanac.seeds[idx + 1]
        end = start + length

        if start <= seed < end:
            return True

    return False


def part1(input: str) -> int:
    almanac = parse_almanac(input, reverse_lookup=False)

    return min(
        location_for_seed(almanac, seed)
        for seed in almanac.seeds
    )


def part2(input: list[str]) -> int:
    almanac = parse_almanac(input, reverse_lookup=True)

    min_location = 0
    while True:
        seed = seed_for_location(almanac, min_location)
        if seed_in_almanac_range(almanac, seed):
            break
        min_location += 1
    return min_location


if __name__ == "__main__":
    run_solution(part1, part2)