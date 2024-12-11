import sys
from typing import Iterable
import unittest

from aoc24.lib.grid import Grid, Point, adjacent_points, build_int_grid

G = Grid[int]


def trailheads(grid: G) -> Iterable[Point]:
    for k, v in grid.items():
        if v == 0:
            yield k


def score_trailhead(t: Point, g: G) -> int:
    visited: set[Point] = set()
    to_visit: set[Point] = set([t])
    result = 0

    while to_visit:
        p = to_visit.pop()
        visited.add(p)

        elevation = g[p]
        for a in adjacent_points(p, g):
            if a in visited:
                continue

            if g[a] - elevation != 1:
                continue

            to_visit.add(a)

        if g[p] == 9:
            result += 1

    return result


def rate_trailhead(t: Point, g: G) -> int:
    approaches: dict[Point, int] = {}
    summits: set[Point] = set()

    to_visit: list[Point] = [t]
    while to_visit:
        p = to_visit.pop()
        approaches.setdefault(p, 0)
        approaches[p] += 1

        elevation = g[p]
        if elevation == 9:
            summits.add(p)
            continue

        for a in adjacent_points(p, g):
            if g[a] - elevation != 1:
                continue

            to_visit.append(a)

    return sum([approaches[x] for x in summits])


def solve_p1(fname: str) -> int:
    g = build_int_grid(fname)
    return sum([score_trailhead(t, g) for t in trailheads(g)])


def solve_p2(fname: str) -> int:
    g = build_int_grid(fname)
    return sum([rate_trailhead(t, g) for t in trailheads(g)])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_10.txt"), 36)

    def test_p2_small(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_10_b.txt"), 13)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_10.txt"), 81)
