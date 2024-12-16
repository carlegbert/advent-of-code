from collections import deque
from itertools import chain
from typing import Iterable, Literal, cast
import unittest

from aoc24.lib.grid import Grid
from aoc24.lib.cartesian import LEFT, RIGHT, Cartesian, cartesian_add

C = Literal["#", "O", ".", "@", "[", "]"]
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


def get_grid_p2(fname: str) -> tuple[G, Cartesian]:
    result: G = {}
    start = (-1, -1)
    with open(fname) as fptr:
        for y, line in enumerate(fptr):
            if line == "\n":
                break
            for x, c in enumerate(line.rstrip()):
                c = cast(C, c)
                result[x * 2, y] = c
                if c == "@":
                    start = x * 2, y
                    c = "."
                elif c == "O":
                    result[x * 2, y] = "["
                    c = "]"
                result[x * 2 + 1, y] = c

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


def displace(start: Cartesian, direction: Cartesian, g: G) -> Cartesian:
    to_check: deque[tuple[Cartesian, C]] = deque([(start, ".")])
    updates: G = {}

    while to_check:
        loc, replacement = to_check.pop()
        if loc in updates:
            continue

        item = g[loc]
        updates[loc] = replacement

        if item == "#":
            return start
        elif item == ".":
            continue

        to_check.append((cartesian_add(loc, direction), item))

        if direction in {LEFT, RIGHT} or item in "@O":
            continue

        offset = LEFT if item == "]" else RIGHT
        neighbor = cartesian_add(loc, offset)
        if neighbor not in updates:
            to_check.appendleft((neighbor, "."))

    g.update(updates)
    return cartesian_add(start, direction)


def gps_sum(g: Grid) -> int:
    return sum([x + 100 * y for (x, y), item in g.items() if item in "O["])


def solve_p1(fname: str) -> int:
    g, start = get_grid(fname)
    for d in get_moves(fname):
        start = displace(start, d, g)
    return gps_sum(g)


def solve_p2(fname: str) -> int:
    g, start = get_grid_p2(fname)
    for d in get_moves(fname):
        start = displace(start, d, g)
    return gps_sum(g)


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_15.txt"), 2028)

    def test_p1_b(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_15_b.txt"), 10092)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_15_b.txt"), 9021)
