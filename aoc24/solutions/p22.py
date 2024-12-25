from collections import deque
import re
import sys
from typing import Deque, Iterable
import unittest


def mix(secret: int, val: int) -> int:
    return secret ^ val


def prune(secret: int) -> int:
    return secret % 16777216


def evolve(secret: int) -> int:
    secret = mix(secret, secret * 64)
    secret = prune(secret)
    secret = mix(secret, secret // 32)
    secret = prune(secret)
    secret = mix(secret, secret * 2048)
    secret = prune(secret)
    return secret


def evolven(secret: int, n: int):
    for _ in range(n):
        secret = evolve(secret)

    return secret


def build_price_list(secret: int) -> Iterable[int]:
    yield secret % 10
    for _ in range(2000):
        secret = evolve(secret)
        yield secret % 10


def build_map(secret: int) -> dict[tuple[int, int, int, int], int]:
    result = {}
    nums: Deque[int] = deque()
    changes: Deque[int] = deque()
    for p in build_price_list(secret):
        nums.append(p)
        if len(nums) == 1:
            continue
        changes.append(p - nums[-2])
        if len(changes) != 5:
            continue
        changes.popleft()
        key = tuple(changes)
        if key in result:
            continue
        result[key] = nums[-1]

    return result


def solve_p1(fname: str) -> int:
    with open(fname) as fptr:
        return sum([evolven(int(line.rstrip()), 2000) for line in fptr])


def solve_p2(fname: str) -> int:
    pricemap = {}
    with open(fname) as fptr:
        for line in fptr:
            x = build_map(int(line.rstrip()))
            for k, v in x.items():
                pricemap[k] = pricemap.get(k, 0) + v

    return max(pricemap.values())


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_22.txt"), 37327623)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_22_b.txt"), 23)
