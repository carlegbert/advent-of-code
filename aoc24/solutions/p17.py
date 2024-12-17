from ast import parse
import re
import unittest


def combo(operand: int, reg: tuple[int, int, int]) -> int:
    a, b, c = reg
    if operand < 4:
        return operand

    if operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c

    raise Exception("bad combo operand")


# Return register A (since B+C are zero in all inputs) and instructions
def parse_input(fname: str):
    with open(fname) as fptr:
        lines = fptr.readlines()
        a = int(re.findall(r"\d+", lines[0])[0])
        return a, [int(m) for m in re.findall(r"\d+", lines[4])]


def run(program: list[int], a=0, b=0, c=0):
    ip = 0
    out = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]
        ip += 2

        match opcode:
            case 0:
                a = a // (2 ** combo(operand, (a, b, c)))
            case 1:
                b = b ^ operand
            case 2:
                b = combo(operand, (a, b, c)) % 8
            case 3:
                if a != 0:
                    ip = operand
            case 4:
                b = b ^ c
            case 5:
                out.append(combo(operand, (a, b, c)) % 8)
            case 6:
                b = a // (2 ** combo(operand, (a, b, c)))
            case 7:
                c = a // (2 ** combo(operand, (a, b, c)))

    return out


def solve_p1(fname: str) -> int:
    a, program = parse_input(fname)
    print(program)
    out = run(program, a)
    s = [str(o) for o in out]
    print(",".join(s))
    return int("".join(s))


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_17.txt"), 4635635210)
