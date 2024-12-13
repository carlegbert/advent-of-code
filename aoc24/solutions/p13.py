from functools import cache
import math
import re
import sys
from typing import Iterable, Union
import unittest


Cartesian = tuple[int, int]
Game = tuple[Cartesian, Cartesian, Cartesian]


INT_REX = r"\d+"


def solve_game(game: Game) -> Union[float, int]:
    a, b, target = game
    x, y = target

    ax, ay = a
    bx, by = b

    asol = bsol = 0

    while 1:
        if x < 0 or y < 0:
            asol = math.inf
            break

        q = x / ax
        if q == y / ay and q == int(q):
            asol += 3 * int(q)
            break
        x -= bx
        y -= by
        asol += 1

    x, y = target
    while 1:
        if x < 0 or y < 0:
            bsol = math.inf
            break

        q = x / bx
        if q == y / by and q == int(q):
            bsol += int(q)
            break
        x -= ax
        y -= ay
        bsol += 3

    return min(asol, bsol)


def get_games(fname: str) -> Iterable[Game]:
    with open(fname) as fptr:
        sections = fptr.read().split("\n\n")
        for section in sections:
            ints = [int(x) for x in re.findall(INT_REX, section)]
            yield (ints[0], ints[1]), (ints[2], ints[3]), (ints[4], ints[5])


def solve_p1(fname: str) -> int:
    coins = [solve_game(game) for game in get_games(fname)]

    return sum([int(c) for c in coins if c != math.inf])


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_13.txt"), 480)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_13.txt"), 0)
