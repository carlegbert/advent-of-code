import functools
import itertools
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


def keypad_to_coords(s: str, keypad: dict[str, Cartesian]) -> tuple[Cartesian, ...]:
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
def paths_between(start: Cartesian, target: Cartesian, layer: int) -> list[str]:
    keyboard = NUMPAD if layer == 0 else ARROWPAD
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


@functools.cache
def get_all_paths(
    points: tuple[Cartesian, ...], start: Cartesian, layer: int
) -> list[str]:
    if not points:
        return []

    target = points[0]
    paths_to_this_node = paths_between(start, target, layer)

    downstream_paths = get_all_paths(tuple(points[1:]), target, layer)
    if not downstream_paths:
        return paths_to_this_node

    result: list[str] = []
    for p in paths_to_this_node:
        result += [p + d for d in downstream_paths]
    return result


def shortest_path(code: str, n: int) -> str:
    p = [NUM_TO_CART[c] for c in code]
    paths = get_all_paths(tuple(p), NUM_TO_CART["A"], 0)
    for layer in range(n):
        paths = itertools.chain(
            *[
                get_all_paths(
                    keypad_to_coords(s, ARROW_TO_CART), ARROW_TO_CART["A"], layer + 1
                )
                for s in paths
            ]
        )

    return min(paths, key=len)


def path_complexity(code: str, n: int) -> int:
    s = shortest_path(code, n)
    return len(s) * int(code[:-1])


def solve_p1(fname: str) -> int:
    with open(fname) as fptr:
        return sum([path_complexity(line.rstrip(), 2) for line in fptr])


def solve_p2(fname: str) -> int:
    with open(fname) as fptr:
        return sum([path_complexity(line.rstrip(), 25) for line in fptr])


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_21.txt"), 126384)
