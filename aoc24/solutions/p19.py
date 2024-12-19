import heapq
from typing import Iterable
import unittest


Towels = dict[int, set[str]]


def available_towels(fname: str) -> Towels:
    with open(fname) as fptr:
        lines = fptr.readlines()
        towels = lines[0].rstrip().split(", ")
        result: Towels = {}
        for t in towels:
            result.setdefault(len(t), set()).add(t)
        return result


def desired_designs(fname: str) -> Iterable[str]:
    with open(fname) as fptr:
        fptr.readline()
        fptr.readline()
        for line in fptr:
            yield line.rstrip()


def designs_possible(design: str, towels: Towels, biggest_towel: int) -> int:
    to_check: list[int] = [0]
    checked = set()
    ways_to_get_there: dict[int, int] = {0: 1}
    while to_check:
        i = heapq.heappop(to_check)

        if i >= len(design) or i in checked:
            continue

        checked.add(i)
        ways_to_get_here = ways_to_get_there[i]

        for n in range(1, biggest_towel + 1):
            end = i + n
            substr = design[i:end]
            t = towels.get(n, set())
            if substr in t:
                ways_to_get_there.setdefault(end, 0)
                ways_to_get_there[end] += ways_to_get_here
                heapq.heappush(to_check, end)

    return ways_to_get_there.get(len(design), 0)


def solve_p1(fname: str) -> int:
    towels = available_towels(fname)
    biggest_towel = max(towels.keys())
    designs = desired_designs(fname)
    count = 0
    for design in designs:
        if designs_possible(design, towels, biggest_towel):
            count += 1
    return count


def solve_p2(fname: str) -> int:
    towels = available_towels(fname)
    biggest_towel = max(towels.keys())
    designs = desired_designs(fname)
    return sum([designs_possible(design, towels, biggest_towel) for design in designs])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_19.txt"), 6)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_19.txt"), 16)
