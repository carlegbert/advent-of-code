Cartesian = tuple[int, int]


LEFT = -1, 0
RIGHT = 1, 0
UP = 0, -1
DOWN = 0, 1

ALL_DIRECTIONS = [LEFT, RIGHT, UP, DOWN]


def cartesian_add(a: Cartesian, b: Cartesian) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx, y + by


def cartesian_add_n(a: Cartesian, b: Cartesian, n: int) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx * n, y + by * n


def is_opposite_direction(a: Cartesian, b: Cartesian) -> bool:
    ax, ay = a
    bx, by = b

    return ax == bx and ay != by or ax != bx and ay == by
