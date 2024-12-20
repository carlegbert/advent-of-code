import itertools
from typing import Iterable
import unittest

from aoc24.lib.cartesian import Cartesian, neighboring_points, points_within_n
from aoc24.lib.grid import adjacent_points, build_grid


Racetrack = dict[Cartesian, int]


def points_within_n_with_distance(
    p: Cartesian, n: int
) -> Iterable[tuple[Cartesian, int]]:
    x, y = p
    for vy in range(-n, n + 1):
        for vx in range(-n, n + 1):
            if vx == 0 and vy == 0:
                continue
            distance = abs(vx) + abs(vy)
            if distance > n:
                continue
            yield (vx + x, vy + y), distance


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


def shortcuts_from_point(p: Cartesian, t: Racetrack, distance: int) -> list[int]:
    start = t[p]
    targets = [(p, d) for p, d in points_within_n_with_distance(p, distance) if p in t]
    distances = [t[p] - d - start for p, d in targets]
    return distances


def solve_p1(fname: str, threshold: int = 100) -> int:
    track, _, _ = get_racetrack(fname)
    positions = track.keys()
    shortcuts = itertools.chain(*[shortcuts_from_point(p, track, 2) for p in positions])
    return len([s for s in shortcuts if s >= threshold])


def solve_p2(fname: str, threshold: int = 100) -> int:
    track, _, _ = get_racetrack(fname)
    positions = track.keys()
    shortcuts = itertools.chain(
        *[shortcuts_from_point(p, track, 20) for p in positions]
    )
    return len([s for s in shortcuts if s >= threshold])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_20.txt", 12), 8)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_20.txt", 72), 29)
