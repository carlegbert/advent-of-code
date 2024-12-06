import sys
import unittest
from typing import TypeVar


Point = tuple[int, int]

T = TypeVar("T")
D = TypeVar("D")

Grid = dict[Point, T]


OBST = "#"
GUARD = "^"


DIRECTIONS: list[Point] = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


def get_guard_start(g: Grid[str]) -> Point:
    for k, v in g.items():
        if v == GUARD:
            return k

    raise ValueError("No guard found!")


def solve_p1(fname: str) -> int:
    grid = build_from_file(fname)
    pos = get_guard_start(grid)
    visited: set[Point] = set()
    dir = 3

    while True:
        visited.add(pos)
        next_pos = add_point(pos, DIRECTIONS[dir])
        next_space = grid.get(next_pos)
        if next_space is None:
            break

        if next_space == OBST:
            dir += 1
            dir %= 4
        else:
            pos = next_pos

    return len(visited)


def solve_p2(fname: str) -> int:
    return 0


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("test_inputs/day_06.txt"), 41)

    def test_p2(self):
        self.assertEqual(solve_p2("test_inputs/day_06.txt"), 6)


def build_from_file(fname: str) -> Grid[str]:
    with open(fname) as fptr:
        g = {}
        for y, line in enumerate(fptr):
            for x, c in enumerate(line):
                g[(x, y)] = c

        return g


def grid_count(g: Grid[T], match: T) -> int:
    return sum([x == match for x in g.values()])


def add_point(a: Point, b: Point) -> Point:
    ax, ay = a
    bx, by = b
    return ax + bx, ay + by


def grid_print(g: Grid) -> None:
    w = max(*[x for x, _ in g.keys()])
    h = max(*[y for _, y in g.keys()])

    for y in range(h):
        for x in range(w):
            print(g[(x, y)], end="")
        print()

    print(f"{w}/{h}")


if __name__ == "__main__":
    filename = "inputs/day_06.txt"
    if len(sys.argv) == 1:
        result = "ERROR: Specify part 1 or 2."
    elif sys.argv[1] == "1":
        result = solve_p1(filename)
    elif sys.argv[1] == "2":
        result = solve_p2(filename)
    else:
        result = "ERROR: Specify part 1 or 2."

    print(result)
