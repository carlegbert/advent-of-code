import heapq
import math
from typing import Literal, cast
import unittest

from aoc24.lib.cartesian import (
    ALL_DIRECTIONS,
    RIGHT,
    Cartesian,
    cartesian_add,
    is_opposite_direction,
)
from aoc24.lib.grid import Grid, build_grid


C = Literal["#", ".", "S", "E"]
G = Grid[C]


def parse_input(fname: str) -> tuple[G, Cartesian, Cartesian]:
    start = end = (-1, -1)
    grid = build_grid(fname)

    for k, v in grid.items():
        if v == "S":
            start = k
        if v == "E":
            end = k

    return grid, start, end


def dijkstra(grid: G, start: Cartesian) -> dict[tuple[Cartesian, Cartesian], int]:
    distances: dict[tuple[Cartesian, Cartesian], int] = {(start, RIGHT): 0}
    h: list[tuple[int, tuple[Cartesian, Cartesian]]] = [(0, (start, RIGHT))]
    visited: set[tuple[Cartesian, Cartesian]] = set()

    while h:
        distance, node = heapq.heappop(h)
        visited.add(node)
        location, direction = node
        moves = [d for d in ALL_DIRECTIONS if not is_opposite_direction(direction, d)]
        moves = [m for m in moves if grid.get(cartesian_add(location, m), "#") != "#"]
        for m in moves:
            new_location = cartesian_add(location, m) if m == direction else location
            key = (new_location, m)
            if key in visited:
                continue

            cost = 1 if m == direction else 1000
            new_distance = distance + cost
            if distances.get(key, math.inf) >= new_distance:
                distances[key] = new_distance
                heapq.heappush(h, (new_distance, key))

    return distances


def solve_p1(fname: str) -> int:
    grid, start, end = parse_input(fname)
    distance_mapping = dijkstra(grid, start)
    return min([distance_mapping[(end, dir)] for dir in ALL_DIRECTIONS])


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_16.txt"), 7036)

    def test_p1_b(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_16_b.txt"), 11048)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_16.txt"), 45)

    def test_p2_b(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_16_b.txt"), 64)
