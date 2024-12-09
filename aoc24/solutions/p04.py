import sys
from typing import Iterator
import unittest


Point = tuple[int, int]
CharMap = dict[Point, str]


def build_map(fname: str) -> CharMap:
    result: CharMap = {}
    with open(fname) as fptr:
        line = ""
        for y, line in enumerate(fptr):
            for x, c in enumerate(line):
                result[(x, y)] = c

    return result


xmas_transforms = [
    lambda x, y, i: (x + i, y),
    lambda x, y, i: (x - i, y),
    lambda x, y, i: (x, y + i),
    lambda x, y, i: (x, y - i),
    lambda x, y, i: (x + i, y + i),
    lambda x, y, i: (x - i, y + i),
    lambda x, y, i: (x + i, y - i),
    lambda x, y, i: (x - i, y - i),
]


def xmas_seqs_from_point(point: Point, cmap: CharMap) -> Iterator[str]:
    start = cmap.get(point, "_")

    x, y = point
    for t in xmas_transforms:
        buf = start
        for i in range(1, 4):
            p = t(x, y, i)
            c = cmap.get(p, "_")
            buf = f"{buf}{c}"

        yield buf


def x_seqs_from_point(point: Point, cmap: CharMap) -> Iterator[str]:
    center = cmap.get(point, "_")

    x, y = point
    ul = cmap.get((x - 1, y - 1), "_")
    dr = cmap.get((x + 1, y + 1), "_")
    ur = cmap.get((x + 1, y - 1), "_")
    dl = cmap.get((x - 1, y + 1), "_")

    yield f"{ul}{center}{dr}"
    yield f"{ur}{center}{dl}"


def solve_p1(fname: str) -> int:
    cmap = build_map(fname)
    result = 0
    for p, c in cmap.items():
        if c != "X":
            continue

        result += sum(
            [candidate == "XMAS" for candidate in xmas_seqs_from_point(p, cmap)]
        )

    return result


def solve_p2(fname: str) -> int:
    cmap = build_map(fname)
    result = 0
    for p, c in cmap.items():
        if c != "A":
            continue

        result += all(
            [candidate in ["MAS", "SAM"] for candidate in x_seqs_from_point(p, cmap)]
        )

    return result


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_04.txt"), 18)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_04.txt"), 9)
