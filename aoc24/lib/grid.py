from typing import Iterable, TypeVar


T = TypeVar("T")

Point = tuple[int, int]
Grid = dict[Point, T]


def build_int_grid(fname: str) -> Grid[int]:
    result: Grid[int] = {}
    with open(fname) as fptr:
        for y, line in enumerate(fptr):
            for x, c in enumerate(line.rstrip()):
                result[(x, y)] = int(c)

    return result


def adjacent_points(p: Point, g: Grid) -> Iterable[Point]:
    x, y = p
    for vx, vy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        a = vx + x, vy + y
        if a in g:
            yield a
