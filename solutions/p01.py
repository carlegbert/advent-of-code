import sys
from collections import Counter
import unittest


def _make_lists(fname: str) -> tuple[list[int], list[int]]:
    list1: list[int] = []
    list2: list[int] = []
    with open(fname) as fptr:
        for line in fptr:
            parts = line.split("   ")
            list1.append(int(parts[0]))
            list2.append(int(parts[1]))

    return list1, list2


def solve_p1(fname: str) -> int:
    lists = _make_lists(fname)
    lists = (sorted(lists[0]), sorted(lists[1]))

    result = 0
    for i, item1 in enumerate(lists[0]):
        result += abs(item1 - lists[1][i])

    return result


def solve_p2(fname: str) -> int:
    lists = _make_lists(fname)
    c = Counter(lists[1])
    return sum([x * c.get(x, 0) for x in lists[0]])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("test_inputs/day_01.txt"), 11)

    def test_p2(self):
        self.assertEqual(solve_p2("test_inputs/day_01.txt"), 31)


if __name__ == "__main__":
    filename = "inputs/day_01.txt"
    if len(sys.argv) == 1:
        result = "ERROR: Specify part 1 or 2."
    elif sys.argv[1] == '1':
        result = solve_p1(filename)
    elif sys.argv[1] == '2':
        result = solve_p2(filename)
    else:
        result = "ERROR: Specify part 1 or 2."

    print(result)
