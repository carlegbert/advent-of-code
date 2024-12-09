from functools import cmp_to_key
import sys
from typing import Iterator
import unittest


RuleMap = dict[int, set[int]]


def build_rule_map(fname: str) -> RuleMap:
    result: RuleMap = {}
    with open(fname) as fptr:
        for line in fptr:
            if line == "\n":
                break

            result.setdefault(int(line[0:2]), set()).add(int(line[3:5]))

    return result


def updates(fname: str) -> Iterator[list[int]]:
    with open(fname) as fptr:
        for line in fptr:
            if line == "\n":
                break

        for line in fptr:
            yield [int(x) for x in line.rstrip().split(",")]


def check_update(rmap: RuleMap, update: list[int]) -> bool:
    before: set[int] = set()

    for num in update:
        items = rmap.get(num, [])
        if any([item in before for item in items]):
            return False

        before.add(num)

    return True


def compare(rmap: RuleMap, left: int, right: int) -> int:
    if right in rmap.get(left, set()):
        return 1
    elif left in rmap.get(right, set()):
        return -1
    else:
        return 0


def fix_update(rmap: RuleMap, update: list[int]) -> list[int]:
    return list(
        sorted(update, key=cmp_to_key(lambda left, right: compare(rmap, left, right)))
    )


def midpoint(update: list[int]) -> int:
    return update[len(update) // 2]


def solve_p1(fname: str) -> int:
    rmap = build_rule_map(fname)
    return sum(
        [midpoint(update) for update in updates(fname) if check_update(rmap, update)]
    )


def solve_p2(fname: str) -> int:
    rmap = build_rule_map(fname)
    return sum(
        [
            midpoint(fix_update(rmap, update))
            for update in updates(fname)
            if not check_update(rmap, update)
        ]
    )


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_05.txt"), 143)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_05.txt"), 123)
