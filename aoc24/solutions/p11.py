from functools import cache
import unittest

from aoc24.lib.numbers import digits


def transform_rock(rock: int) -> list[int]:
    if rock == 0:
        return [1]

    n = digits(rock)

    if n % 2 == 0:
        f = 10 ** (n // 2)
        left, right = divmod(rock, f)
        return [left, right]

    return [rock * 2024]


def parse_input(fname: str) -> list[int]:
    with open(fname) as fptr:
        return [int(x) for x in fptr.read().split(" ")]


@cache
def num_of_rocks(rock: int, blinks: int) -> int:
    if blinks == 0:
        return 1

    blinks -= 1
    rocks = transform_rock(rock)
    result = sum([num_of_rocks(r, blinks) for r in rocks])
    return result


def solve_p1(fname: str) -> int:
    return sum([
        num_of_rocks(rock, 25)
        for rock in parse_input(fname)
    ])

def solve_p2(fname: str) -> int:
    return sum([
        num_of_rocks(rock, 75)
        for rock in parse_input(fname)
    ])


class TestCase(unittest.TestCase):
    def test_transform_rocks(self):
        self.assertEqual(transform_rock(0), [1])
        self.assertEqual(transform_rock(1), [2024])
        self.assertEqual(transform_rock(10), [1, 0])
        self.assertEqual(transform_rock(99), [9, 9])
        self.assertEqual(transform_rock(999), [2021976])

    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_11.txt"), 55312)
