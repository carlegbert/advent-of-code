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


def dijkstra(grid: G, start: Cartesian, end: Cartesian) -> tuple[int, set[Cartesian]]:
    distances: dict[tuple[Cartesian, Cartesian], int] = {(start, RIGHT): 0}
    # lazy but effective: just keep track of the path.
    h: list[tuple[int, tuple[Cartesian, Cartesian], set[Cartesian]]] = [
        (0, (start, RIGHT), set([start]))
    ]
    visited: set[tuple[Cartesian, Cartesian]] = set()
    best = math.inf
    good_seats: set[Cartesian] = set()

    while h:
        distance, node, path = heapq.heappop(h)
        visited.add(node)
        if distance > best:
            continue

        location, direction = node

        if location == end:
            if distance < best:
                best = distance
                good_seats = path
            elif distance == best:
                good_seats = good_seats.union(path)
            continue

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
                heapq.heappush(h, (new_distance, key, path.union([new_location])))

    return int(best), good_seats


def solve_p1(fname: str) -> int:
    grid, start, end = parse_input(fname)
    result, _ = dijkstra(grid, start, end)
    return result


def solve_p2(fname: str) -> int:
    grid, start, end = parse_input(fname)
    _, good_seats = dijkstra(grid, start, end)
    return len(good_seats)


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_16.txt"), 7036)

    def test_p1_b(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_16_b.txt"), 11048)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_16.txt"), 45)

    def test_p2_b(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_16_b.txt"), 64)
