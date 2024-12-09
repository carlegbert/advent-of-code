import unittest
from typing import Optional


def build_fs(input: str) -> list[Optional[int]]:
    isfile = True
    id = 0
    result = []
    for c in input.rstrip():
        val = id if isfile else None
        for _ in range(int(c)):
            result.append(val)

        id += isfile
        isfile = not isfile

    return result


def checksum(fs: list[Optional[int]]) -> int:
    return sum([i * item for i, item in enumerate(fs) if item is not None])


def compress(fs: list[Optional[int]]) -> None:
    leftptr, rightptr = 0, len(fs) - 1

    while leftptr < rightptr:
        if fs[leftptr] is not None:
            leftptr += 1
            continue

        if fs[rightptr] is None:
            rightptr -= 1
            continue

        fs[leftptr], fs[rightptr] = fs[rightptr], fs[leftptr]
        leftptr += 1
        rightptr -= 1


def solve_p1(fname: str) -> int:
    fptr = open(fname)
    input = fptr.read()
    fptr.close()

    fs = build_fs(input)
    compress(fs)
    return checksum(fs)


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_09.txt"), 1928)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_09.txt"), 2858)
