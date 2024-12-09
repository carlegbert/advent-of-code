import re
import sys
from typing import Iterator
import unittest


mul_rex = "mul\\(\\d{1,3},\\d{1,3}\\)"
do_rex = "do\\(\\)"
dont_rex = "don't\\(\\)"
expr_rex = f"({mul_rex}|{do_rex}|{dont_rex})"


def get_valid_mul_exprs(s: str) -> list[str]:
    return re.findall(mul_rex, s)


def eval_mul_expr(expr: str) -> int:
    a, b = re.findall(r"\d+", expr)
    return int(a) * int(b)


def solve_p1(fname: str) -> int:
    with open(fname) as fptr:
        exprs = get_valid_mul_exprs(fptr.read())
        return sum([eval_mul_expr(expr) for expr in exprs])


def solve_p2(fname: str) -> int:
    with open(fname) as fptr:
        enabled = True
        result = 0
        for expr in re.findall(expr_rex, fptr.read()):
            if re.match(mul_rex, expr) and enabled:
                result += eval_mul_expr(expr)
            elif re.match(do_rex, expr):
                enabled = True
            else:
                enabled = False

        return result


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_03.txt"), 161)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_03b.txt"), 48)
