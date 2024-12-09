import sys
import unittest
from typing import TypeVar


Point = tuple[int, int]

T = TypeVar("T")
D = TypeVar("D")

Grid = dict[Point, T]


OBST = "#"
GUARD = "^"
EMPTY = "."


DIRECTIONS: list[Point] = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


class InfiniteLoopError(Exception):
    pass


def get_guard_start(g: Grid[str]) -> Point:
    for k, v in g.items():
        if v == GUARD:
            return k

    raise ValueError("No guard found!")


def get_guard_path(grid: Grid, pos: Point) -> set[Point]:
    visited: dict[Point, set[int]] = {}
    dir = 3

    while True:
        previous_visits = visited.setdefault(pos, set())
        if dir in previous_visits:
            raise InfiniteLoopError
        else:
            previous_visits.add(dir)

        next_pos = add_point(pos, DIRECTIONS[dir])
        next_space = grid.get(next_pos)
        if next_space is None:
            break

        if next_space == OBST:
            dir += 1
            dir %= 4
        else:
            pos = next_pos

    return set(visited.keys())


def solve_p1(fname: str) -> int:
    grid = build_from_file(fname)
    start = get_guard_start(grid)

    return len(get_guard_path(grid, start))


def solve_p2(fname: str) -> int:
    grid = build_from_file(fname)
    start = get_guard_start(grid)

    guard_path = get_guard_path(grid, start)
    guard_path.remove(start)

    result = 0

    for point in guard_path:
        grid[point] = OBST

        try:
            get_guard_path(grid, start)
        except InfiniteLoopError:
            result += 1

        grid[point] = EMPTY

    return result


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_06.txt"), 41)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_06.txt"), 6)


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
