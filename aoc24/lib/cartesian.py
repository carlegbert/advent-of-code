Cartesian = tuple[int, int]


def cartesian_add(a: Cartesian, b: Cartesian) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx, y + by


def cartesian_add_n(a: Cartesian, b: Cartesian, n: int) -> Cartesian:
    x, y = a
    bx, by = b
    return x + bx * n, y + by * n
