from typing import Callable, Iterable, TypeVar

from aoc24.lib.cartesian import Cartesian


T = TypeVar("T")

Grid = dict[Cartesian, T]


def build_grid(fname: str, f: Callable = str) -> Grid:
    result: Grid = {}
    with open(fname) as fptr:
        for y, line in enumerate(fptr):
            for x, c in enumerate(line.rstrip()):
                result[(x, y)] = f(c)

    return result


def adjacent_points(p: Cartesian, g: Grid) -> Iterable[Cartesian]:
    x, y = p
    for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        a = vx + x, vy + y
        if a in g:
            yield a
