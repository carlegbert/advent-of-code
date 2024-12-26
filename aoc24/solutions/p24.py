from collections import deque
from typing import Iterable, Literal, cast
import unittest


Operator = Literal["AND", "XOR", "OR"]
Operation = tuple[str, str, Operator, str]


def initial_inputs(fname: str) -> dict[str, bool]:
    result = {}
    with open(fname) as f:
        for line in f:
            if line == "\n":
                break

            left, right = line.rstrip().split(":")
            right = right[1] == "1"
            result[left] = right

        return result


def operations(fname) -> Iterable[Operation]:
    with open(fname) as fptr:
        for line in fptr:
            if line == "\n":
                break

        for line in fptr:
            op1, operator, op2, _, dest = line.rstrip().split(" ")

            yield op1, op2, cast(Operator, operator), dest


def get_result(operation: Operation, state: dict[str, bool]) -> bool:
    op1, op2, operator, _ = operation
    op1, op2 = state[op1], state[op2]
    if operator == "XOR":
        return op1 != op2
    elif operator == "AND":
        return op1 and op2
    else:
        return op1 or op2


def solve_p1(fname: str) -> int:
    state = initial_inputs(fname)
    result = 0
    q = deque(operations(fname))
    while q:
        operation = q.popleft()
        op1, op2, _, dest = operation
        if op1 not in state or op2 not in state:
            q.append(operation)
            continue

        state[dest] = get_result(operation, state)
        if dest[0] == "z":
            offset = int(dest[1:])
            result |= state[dest] << offset

    return result


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_24.txt"), 4)

    def test_p2(self):
        self.assertEqual(solve_p2("test_inputs/day_24.txt"), 0)
