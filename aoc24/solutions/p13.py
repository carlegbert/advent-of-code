import math
import re
from typing import Iterable, Optional
import unittest


Cartesian = tuple[int, int]
Game = tuple[Cartesian, Cartesian, Cartesian]


INT_REX = r"\d+"
TEN_BILLION_DOLLARS = 10_000_000_000_000


# https://en.wikipedia.org/wiki/Cramer%27s_rule
def solve_game(game: Game) -> Optional[int]:
    a, b, target = game
    x, y = target

    ax, ay = a
    bx, by = b

    a_presses = (x * by - y * bx) / (ax * by - ay * bx)
    b_presses = (y * ax - x * ay) / (ax * by - ay * bx)

    result = a_presses * 3 + b_presses
    rounded = int(result)
    return rounded if rounded == result else None


def get_games(fname: str, padding: int = 0) -> Iterable[Game]:
    with open(fname) as fptr:
        sections = fptr.read().split("\n\n")
        for section in sections:
            ints = [int(x) for x in re.findall(INT_REX, section)]
            a = ints[0], ints[1]
            b = ints[2], ints[3]
            x, y = ints[4], ints[5]
            yield a, b, (x + padding, y + padding)


def solve_p1(fname: str) -> int:
    coins = [solve_game(game) for game in get_games(fname)]

    return sum([int(c) for c in coins if c is not None])


def solve_p2(fname: str) -> int:
    coins = [solve_game(game) for game in get_games(fname, TEN_BILLION_DOLLARS)]

    return sum([int(c) for c in coins if c is not None])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_13.txt"), 480)
