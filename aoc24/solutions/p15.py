from itertools import chain
from typing import Iterable, Literal, cast
import unittest

from aoc24.lib.grid import Grid
from aoc24.lib.cartesian import Cartesian, cartesian_add

C = Literal["#", "O", ".", "@"]
G = Grid[C]


def get_grid(fname: str) -> tuple[G, Cartesian]:
    result: G = {}
    start = (-1, -1)
    with open(fname) as fptr:
        for y, line in enumerate(fptr):
            if line == "\n":
                break
            for x, c in enumerate(line.rstrip()):
                result[x, y] = cast(C, c)
                if c == "@":
                    start = x, y

        return result, start


def get_moves(fname: str) -> Iterable[Cartesian]:
    with open(fname) as fptr:
        for line in fptr:
            if line == "\n":
                break

        for c in chain.from_iterable(fptr):
            if c == "<":
                yield -1, 0
            elif c == ">":
                yield 1, 0
            elif c == "^":
                yield 0, -1
            elif c == "v":
                yield 0, 1


def move_item(loc: Cartesian, direction: Cartesian, replacement: C, g: G) -> bool:
    item = g.get(loc, "#")
    if item == "#":
        return False

    if item == "." or move_item(cartesian_add(loc, direction), direction, item, g):
        g[loc] = replacement
        return True

    return False


def gps_sum(g: Grid) -> int:
    return sum([x + 100 * y for (x, y), item in g.items() if item == "O"])


def solve_p1(fname: str) -> int:
    g, start = get_grid(fname)
    for d in get_moves(fname):
        if move_item(start, d, ".", g):
            start = cartesian_add(start, d)
    return gps_sum(g)


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_15.txt"), 2028)

    def test_p1_b(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_15_b.txt"), 10092)

    def test_p2(self):
        self.assertEqual(solve_p2("test_inputs/day_15_b.txt"), 9021)
