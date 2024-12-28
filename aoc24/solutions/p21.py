import functools
import heapq
import unittest

from aoc24.lib.cartesian import DOWN, LEFT, RIGHT, UP, Cartesian, cartesian_add

NUMPAD: dict[Cartesian, str] = {
    (0, 0): "7",
    (1, 0): "8",
    (2, 0): "9",
    (0, 1): "4",
    (1, 1): "5",
    (2, 1): "6",
    (0, 2): "1",
    (1, 2): "2",
    (2, 2): "3",
    (1, 3): "0",
    (2, 3): "A",
}

ARROWPAD: dict[Cartesian, str] = {
    (1, 0): "^",
    (2, 0): "A",
    (0, 1): "<",
    (1, 1): "v",
    (2, 1): ">",
}

NUM_TO_CART = {v: k for k, v in NUMPAD.items()}
ARROW_TO_CART = {v: k for k, v in ARROWPAD.items()}


def keypad_to_coords(s: str, is_numpad: bool) -> tuple[Cartesian, ...]:
    keypad = NUM_TO_CART if is_numpad else ARROW_TO_CART
    return tuple([keypad[c] for c in s])


def path_valid(point: Cartesian, path: str, keypad: dict[Cartesian, str]) -> bool:
    for c in path:
        if point not in keypad:
            return False

        if c == "<":
            point = cartesian_add(LEFT, point)
        elif c == ">":
            point = cartesian_add(RIGHT, point)
        elif c == "^":
            point = cartesian_add(UP, point)
        elif c == "v":
            point = cartesian_add(DOWN, point)

    return True


@functools.cache
def paths_between_keys(_start: str, _target: str, is_numpad: bool) -> list[str]:
    keyboard = NUMPAD if is_numpad else ARROWPAD
    start = keypad_to_coords(_start, is_numpad)[0]
    target = keypad_to_coords(_target, is_numpad)[0]
    tx, ty = target
    sx, sy = start

    h = v = ""
    h += ">" * (tx - sx)
    h += "<" * (sx - tx)
    v += "v" * (ty - sy)
    v += "^" * (sy - ty)

    paths_to_this_node = [h + v + "A"]
    if h and v:
        paths_to_this_node += [v + h + "A"]

    return [p for p in paths_to_this_node if path_valid(start, p, keyboard)]


def best_path(key_combo: str, n: int, is_numpad: bool) -> str:
    if n == 0:
        return key_combo

    result = ""
    for start, target in zip('A' + key_combo[:-1], key_combo):
        candidates = paths_between_keys(start, target, is_numpad)
        best = min([best_path(c, n - 1, False) for c in candidates])
        result += best

    return result


def path_complexity(code: str, path: str) -> int:
    return len(path) * int(code[:-1])


def solve_p1(fname: str) -> int:
    with open(fname) as fptr:
        return sum(
            [
                path_complexity(line.rstrip(), best_path(line.rstrip(), 3, True))
                for line in fptr
            ]
        )


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_21.txt"), 126384)
