import itertools
import unittest

from aoc24.lib.cartesian import Cartesian, neighboring_points
from aoc24.lib.grid import adjacent_points, build_grid


Racetrack = dict[Cartesian, int]


def get_racetrack(fname: str) -> tuple[Racetrack, Cartesian, Cartesian]:
    start = end = -1, -1
    grid = build_grid(fname)
    for k, v in grid.items():
        if v == "S":
            start = k
        if v == "E":
            end = k

    result = {start: 0}
    node = start
    count = 0
    while node != end:
        grid[node] = "#"
        count += 1
        for n in adjacent_points(node, grid):
            if grid[n] != "#":
                node = n
                continue

        result[node] = count

    return result, start, end


def shortcuts_from_point(p: Cartesian, t: Racetrack) -> set[int]:
    start = t[p]
    walls = [n for n in neighboring_points(p) if n not in t]
    shortcut_dests = itertools.chain(*[neighboring_points(w) for w in walls])
    reachable = [s for s in shortcut_dests if s in t]
    return set([t[p] - start - 2 for p in reachable])


def solve_p1(fname: str, threshold: int = 100) -> int:
    track, _, _ = get_racetrack(fname)
    positions = track.keys()
    shortcuts = itertools.chain(*[shortcuts_from_point(p, track) for p in positions])
    return len([s for s in shortcuts if s >= threshold])


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_20.txt", 12), 8)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_20.txt"), 0)
