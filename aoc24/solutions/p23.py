import itertools
from typing import Iterable
import unittest


AdjacencyMap = dict[str, set[str]]


def connections(fname: str) -> Iterable[tuple[str, str]]:
    with open(fname) as fptr:
        for line in fptr:
            a, b = line.rstrip().split("-")
            yield a, b


def build_adjacency_map(fname: str) -> AdjacencyMap:
    result: AdjacencyMap = {}
    for a, b in connections(fname):
        result.setdefault(a, set()).add(b)
        result.setdefault(b, set()).add(a)

    return result


def dense_groups(m: AdjacencyMap) -> Iterable[set[str]]:
    for k, v in m.items():
        group = set([k])
        for x in v:
            if m[x] >= group:
                group.add(x)
        yield group


def cycles(key: str, m: AdjacencyMap) -> set[tuple[str, str, str]]:
    result = set()
    for n1 in m[key]:
        for n2 in m[n1]:
            if key in m[n2]:
                result.add(tuple(sorted([key, n1, n2])))

    return result


def solve_p1(fname: str) -> int:
    m = build_adjacency_map(fname)
    ts = [x for x in m.keys() if x[0] == "t"]
    result: set[tuple[str, str, str]] = set()
    for t in ts:
        c = set([x for x in cycles(t, m) if len(x) == 3])
        result |= c

    return len(result)


def solve_p2(fname: str) -> str:
    m = build_adjacency_map(fname)
    group = max(dense_groups(m), key=len)
    return ",".join(sorted(group))


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_23.txt"), 7)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_23.txt"), "co,de,ka,ta")
