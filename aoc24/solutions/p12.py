from typing import Iterable
import unittest

from aoc24.lib.grid import Grid, Point, adjacent_points, build_grid


G = Grid[str]


RIGHT = 1j
LEFT = -1j
UP = -2j
DOWN = 2j


def adjacent_plots(p: Point, region: set[Point]) -> list[Point]:
    x, y = p
    return [
        (vx + x, vy + y)
        for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if (vx + x, vy + y) in region
    ]


def region_perimeter(r: set[Point]) -> int:
    return sum([4 - len(adjacent_plots(p, r)) for p in r])


def count_continuous_ranges(items: list[int]) -> int:
    count = 0
    items = sorted(items)
    prev = None
    while items:
        item = items.pop()
        if item + 1 != prev:
            count += 1
        prev = item

    return count


def region_edges(r: set[Point]) -> int:
    edge_sections: dict[complex, list[int]] = {}
    for p in r:
        a = adjacent_plots(p, r)
        x, y = p
        # Adding complex numbers is a quick way to keep each orientation
        # separate in the edge_sections dict.
        if (x + 1, y) not in a:
            edge_sections.setdefault(x + RIGHT, []).append(y)
        if (x - 1, y) not in a:
            edge_sections.setdefault(x + LEFT, []).append(y)
        if (x, y + 1) not in a:
            edge_sections.setdefault(y + DOWN, []).append(x)
        if (x, y - 1) not in a:
            edge_sections.setdefault(y + UP, []).append(x)

    return sum([count_continuous_ranges(x) for x in edge_sections.values()])


def get_regions(g: G) -> Iterable[set[Point]]:
    to_visit: set[Point] = set(g)
    to_visit_in_region: list[Point] = [to_visit.pop()]
    region_label: str = g[to_visit_in_region[0]]
    region: set[Point] = set()

    while to_visit_in_region:
        node = to_visit_in_region.pop()

        to_visit.discard(node)
        region.add(node)

        adj = adjacent_points(node, g)
        for a in adj:
            if a in region or g[a] != region_label:
                continue

            to_visit_in_region.append(a)

        if not to_visit_in_region:
            yield region
            if not to_visit:
                return

            to_visit_in_region.append(to_visit.pop())
            region_label = g[to_visit_in_region[0]]
            region = set()


def solve_p1(fname: str) -> int:
    g = build_grid(fname)
    return sum([len(r) * region_perimeter(r) for r in get_regions(g)])


def solve_p2(fname: str) -> int:
    g = build_grid(fname)
    return sum([len(r) * region_edges(r) for r in get_regions(g)])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_12.txt"), 140)

    def test_p1_larger(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_12_b.txt"), 1930)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_12.txt"), 80)

    def test_p2_larger(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_12_b.txt"), 1206)

    def test_get_region_sides(self):
        self.assertEqual(region_edges(set([(0, 0), (0, 1), (0, 2), (0, 3)])), 4)
