import sys
import unittest


def _reports(fname: str):
    with open(fname) as fptr:
        for line in fptr:
            yield [int(x) for x in line.split()]


def _report_valid(report: list[int], skip_idx: int) -> bool:
    prev = None
    ascents = descents = 0

    for i, cur in enumerate(report):
        if i == skip_idx:
            continue

        if prev is None:
            prev = cur
            continue

        diff = cur - prev
        if abs(diff) > 3:
            return False

        if diff == 0:
            return False

        if diff > 0:
            ascents += 1
        else:
            descents += 1

        if ascents and descents:
            return False

        prev = cur

    return True


def report_valid(report: list[int], can_skip=False) -> bool:
    initial_result = _report_valid(report, -1)
    if not can_skip:
        return initial_result

    return any([_report_valid(report, i) for i, _ in enumerate(report)])


def solve_p1(fname: str) -> int:
    return sum([report_valid(x) for x in _reports(fname)])


def solve_p2(fname: str) -> int:
    return sum([report_valid(x, True) for x in _reports(fname)])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_02.txt"), 2)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_02.txt"), 4)
