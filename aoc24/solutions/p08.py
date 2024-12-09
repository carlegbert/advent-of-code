from typing import Iterator
import sys
import unittest


Point = tuple[int, int]


def compute_antinodes(a: Point, b: Point) -> set[Point]:
    ax, ay = a
    bx, by = b
    vx, vy = ax - bx, ay - by

    return set([(ax + vx, ay + vy), (bx - vx, by - vy)])


def compute_harmonic_antinodes(a: Point, b: Point, size: int) -> set[Point]:
    ax, ay = a
    bx, by = b
    vx, vy = ax - bx, ay - by

    x, y = ax, ay
    result = set()
    while x >= 0 and x < size and y >= 0 and y < size:
        result.add((x, y))
        x += vx
        y += vy

    return result


def antenna_iter(fname: str) -> Iterator[tuple[str, Point]]:
    fptr = open(fname)
    for y, line in enumerate(fptr):
        for x, c in enumerate(line.strip()):
            if c == ".":
                continue

            yield c, (x, y)

    fptr.close()


def get_size(fname: str) -> int:
    with open(fname, "rb") as fptr:
        return sum(1 for _ in fptr)


def solve_p1(fname: str) -> int:
    antenna_map: dict[str, set[Point]] = {}
    antinodes: set[Point] = set()

    size = get_size(fname)

    for c, loc in antenna_iter(fname):
        if c in antenna_map:
            for p in antenna_map[c]:
                antinodes.update(compute_antinodes(loc, p))
        else:
            antenna_map[c] = set()

        antenna_map[c].add(loc)

    inbounds_antinodes = [
        (x, y) for x, y in antinodes if x >= 0 and x < size and y >= 0 and y < size
    ]

    return len(inbounds_antinodes)


def solve_p2(fname: str) -> int:
    antenna_map: dict[str, set[Point]] = {}
    antinodes: set[Point] = set()
    size = get_size(fname)

    for c, antenna_loc in antenna_iter(fname):
        if c in antenna_map:
            for matching_antenna in antenna_map[c]:
                antinodes.update(compute_harmonic_antinodes(antenna_loc, matching_antenna, size))
                antinodes.update(compute_harmonic_antinodes(matching_antenna, antenna_loc, size))
        else:
            antenna_map[c] = set()

        antenna_map[c].add(antenna_loc)

    return len(antinodes)


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_08.txt"), 14)

    def test_p2_small(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_08_b.txt"), 9)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_08.txt"), 34)
