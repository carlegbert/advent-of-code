from itertools import islice
import heapq
from typing import Iterable
import unittest

from aoc24.lib.cartesian import ALL_DIRECTIONS, Cartesian, cartesian_add


def parse_input(fname: str) -> Iterable[Cartesian]:
    with open(fname) as f:
        for line in f:
            a, b = line.split(",")
            yield int(a), int(b)


def neighbors(
    pos: Cartesian, size: int, corrupted: set[Cartesian]
) -> Iterable[Cartesian]:
    for d in ALL_DIRECTIONS:
        n = cartesian_add(pos, d)
        x, y = n
        if x < 0 or x >= size or y < 0 or y >= size:
            continue
        if n in corrupted:
            continue
        yield n


def shortest_path(mem: set[Cartesian], size: int) -> set[Cartesian]:
    end = size - 1, size - 1

    visited = set()
    start = 0, 0
    to_visit: list[tuple[int, Cartesian, set[Cartesian]]] = [(0, start, set([start]))]
    while to_visit:
        s, node, path = heapq.heappop(to_visit)
        if node in visited:
            continue
        if node == end:
            return path

        visited.add(node)
        for n in neighbors(node, size, mem):
            new_path: set[Cartesian] = path | set([node])
            heapq.heappush(to_visit, (s + 1, n, new_path))

    return set()


def solve_p1(fname: str, size=71, b=1024) -> int:
    g = parse_input(fname)
    corrupted_memory = set(islice(g, b))
    return len(shortest_path(corrupted_memory, size))


def solve_p2(fname: str, size=71, b=1024) -> str:
    g = parse_input(fname)
    corrupted_memory = set(islice(g, b - 1))
    path = shortest_path(corrupted_memory, size)
    for m in g:
        corrupted_memory.add(m)
        if m in path:
            path = shortest_path(corrupted_memory, size)
        if not path:
            x, y = m
            return f"{x},{y}"

    return "<not found>"


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_18.txt", 7, 12), 22)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_18.txt", 7, 12), "6,1")
