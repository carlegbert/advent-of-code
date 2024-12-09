import math
import sys
from typing import Iterator
import unittest


Equation = tuple[int | int, list[int]]


def get_equations(fname: str) -> Iterator[Equation]:
    fptr = open(fname)
    for line in fptr:
        testval, rest = line.split(":")
        testval = int(testval)
        nums = rest.strip().split(" ")
        yield testval, [int(num) for num in nums]

    fptr.close()


def digits(n: int) -> int:
    return int(math.log10(n)) + 1


def equation_possibly_true(e: Equation, include_concat=False) -> bool:
    testval, nums = e

    *nums, num = nums
    if not nums:
        return num == testval

    quotient, remainder = divmod(testval, num)
    is_int = remainder == 0
    result = is_int and equation_possibly_true((quotient, nums), include_concat)
    result = result or equation_possibly_true((testval - num, nums), include_concat)

    if include_concat:
        d = digits(num)
        q, r = divmod(testval, 10**d)
        result = (
            result or r == num and equation_possibly_true((q, nums), include_concat)
        )

    return result


def solve_p1(fname: str) -> int:
    return sum([e[0] for e in get_equations(fname) if equation_possibly_true(e)])


def solve_p2(fname: str) -> int:
    return sum([e[0] for e in get_equations(fname) if equation_possibly_true(e, True)])


class TestCase(unittest.TestCase):
    def test_possiby_valid_multiple_solutions(self):
        e = (3267, [81, 40, 27])
        result = equation_possibly_true(e)
        self.assertTrue(result)

    def test_p1(self):
        self.assertEqual(solve_p1("test_inputs/day_07.txt"), 3749)

    def test_p2(self):
        self.assertEqual(solve_p2("test_inputs/day_07.txt"), 11387)


if __name__ == "__main__":
    filename = "inputs/day_07.txt"
    if len(sys.argv) == 1:
        result = "ERROR: Specify part 1 or 2."
    elif sys.argv[1] == "1":
        result = solve_p1(filename)
    elif sys.argv[1] == "2":
        result = solve_p2(filename)
    else:
        result = "ERROR: Specify part 1 or 2."

    print(result)
