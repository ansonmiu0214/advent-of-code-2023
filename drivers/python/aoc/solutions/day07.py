# built-in
from collections import Counter
from enum import IntEnum, auto
from dataclasses import dataclass
from functools import total_ordering
from typing import ClassVar, Type, cast

# project
from aoc.helpers.runnerlib import run_solution


class HandTypes(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIRS = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


def parse_hands[HandType](input: str, *, as_type: Type[HandTypes]) -> list[HandType]:
    hands: list[HandType] = []
    for line in input.splitlines():
        cards, bid = line.split(" ")
        hands.append(as_type(tuple(cards), int(bid)))
    return hands


def part1(input: str) -> int:
    @total_ordering
    @dataclass(frozen=True)
    class Hand:
        cards: tuple[str]
        bid: int

        _CARDS_ORDERED_IN_ASCENDING_STRENGTH: ClassVar = "23456789TJQKA"

        @classmethod
        @property
        def _CARD_TO_STRENGTH(cls) -> dict[str, int]:
            return {
                card: strength
                for strength, card in enumerate(cls._CARDS_ORDERED_IN_ASCENDING_STRENGTH)
            }

        @property
        def type(self) -> HandTypes:
            unique_card_counts = Counter(self.cards)
            if len(unique_card_counts) == 1:
                return HandTypes.FIVE_OF_A_KIND
        
            [(_, freq_of_most_common_card)] = unique_card_counts.most_common(1)
            if len(unique_card_counts) == 2:
                if freq_of_most_common_card == 4:
                    return HandTypes.FOUR_OF_A_KIND
                else:
                    return HandTypes.FULL_HOUSE
            
            if len(unique_card_counts) == 3:
                if freq_of_most_common_card == 3:
                    return HandTypes.THREE_OF_A_KIND
                else:
                    return HandTypes.TWO_PAIRS
            
            if len(unique_card_counts) == 4:
                return HandTypes.ONE_PAIR
            else:
                return HandTypes.HIGH_CARD
        
        def __eq__(self, __value: object) -> bool:
            if type(self) is not type(__value):
                return False
            
            other = cast(Hand, __value)
            return self.cards == other.cards

        def __lt__(self, __value: object) -> bool:
            assert type(self) is type(__value)

            other = cast(Hand, __value)
            if self.type != other.type:
                return self.type < other.type

            for my_card, their_card in zip(self.cards, other.cards):
                if self._CARD_TO_STRENGTH[my_card] != self._CARD_TO_STRENGTH[their_card]:
                    return self._CARD_TO_STRENGTH[my_card] < self._CARD_TO_STRENGTH[their_card]
            
            # we're equal!
            return False

    hands = parse_hands(input, as_type=Hand)
    ranked_hands = sorted(hands)
    winnings_per_hand = [
        rank * hand.bid
        for rank, hand in enumerate(ranked_hands, start=1)
    ]
    return sum(winnings_per_hand)


def part2(input: str) -> int:
    JOKER = "J"

    @total_ordering
    @dataclass(frozen=True)
    class Hand:
        cards: tuple[str]
        bid: int

        _CARDS_ORDERED_IN_ASCENDING_STRENGTH: ClassVar = "J23456789TQKA"

        @classmethod
        @property
        def _CARD_TO_STRENGTH(cls) -> dict[str, int]:
            return {
                card: strength
                for strength, card in enumerate(cls._CARDS_ORDERED_IN_ASCENDING_STRENGTH)
            }

        @property
        def type(self) -> HandTypes:
            unique_card_counts = Counter(self.cards)
            if len(unique_card_counts) == 1:
                return HandTypes.FIVE_OF_A_KIND
        
            [(_, freq_of_most_common_card)] = unique_card_counts.most_common(1)
            if len(unique_card_counts) == 2:
                if JOKER in unique_card_counts:
                    # JJJJ+A -> AAAAA
                    # JJJ+AA -> AAAAA
                    # AA+JJJ -> AAAAAA
                    return HandTypes.FIVE_OF_A_KIND

                elif freq_of_most_common_card == 4:
                    return HandTypes.FOUR_OF_A_KIND
                else:
                    return HandTypes.FULL_HOUSE
            
            if len(unique_card_counts) == 3:
                if freq_of_most_common_card == 3:
                    if JOKER in unique_card_counts:
                        # JJJ+AB -> AAAAB
                        # AAA+JB -> AAAAB
                        return HandTypes.FOUR_OF_A_KIND
                    else:
                        return HandTypes.THREE_OF_A_KIND
                
                if JOKER in unique_card_counts:
                    # JJAAB -> AAAAB
                    # AABBJ -> AAABB
                    if unique_card_counts[JOKER] == 2:
                        return HandTypes.FOUR_OF_A_KIND
                    else:
                        return HandTypes.FULL_HOUSE
                else:
                    return HandTypes.TWO_PAIRS
            
            if len(unique_card_counts) == 4:
                if JOKER in unique_card_counts:
                    # JAABC -> AAABC
                    # JJABC -> AAABC
                    return HandTypes.THREE_OF_A_KIND
                else:
                    return HandTypes.ONE_PAIR
            
            if JOKER in unique_card_counts:
                return HandTypes.ONE_PAIR
            else:    
                return HandTypes.HIGH_CARD
        
        def __eq__(self, __value: object) -> bool:
            if type(self) is not type(__value):
                return False
            
            other = cast(Hand, __value)
            return self.cards == other.cards

        def __lt__(self, __value: object) -> bool:
            assert type(self) is type(__value)

            other = cast(Hand, __value)
            if self.type != other.type:
                return self.type < other.type

            for my_card, their_card in zip(self.cards, other.cards):
                if self._CARD_TO_STRENGTH[my_card] != self._CARD_TO_STRENGTH[their_card]:
                    return self._CARD_TO_STRENGTH[my_card] < self._CARD_TO_STRENGTH[their_card]
            
            # we're equal!
            return False

    hands = parse_hands(input, as_type=Hand)
    ranked_hands = sorted(hands)
    winnings_per_hand = [
        rank * hand.bid
        for rank, hand in enumerate(ranked_hands, start=1)
    ]
    return sum(winnings_per_hand)


if __name__ == "__main__":
    run_solution(part1, part2)