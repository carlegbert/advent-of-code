Cartesian = tuple[int, int]


LEFT = -1, 0
RIGHT = 1, 0
UP = 0, -1
DOWN = 0, 1


def cartesian_add(a: Cartesian, b: Cartesian) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx, y + by


def cartesian_add_n(a: Cartesian, b: Cartesian, n: int) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx * n, y + by * n
