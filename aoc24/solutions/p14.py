import re
from typing import Iterable
import unittest

from aoc24.lib.cartesian import Cartesian, cartesian_add_n, cartesian_add


WIDTH = 101
HEIGHT = 103


Robot = tuple[Cartesian, Cartesian]


def longest_vertical_run(robots: list[Robot], w: int, h: int) -> int:
    positions = set([pos for pos, _ in robots])
    runs: set[int] = set()
    for x in range(w):
        count = 1
        for y in range(h + 1):
            if (x, y) not in positions:
                runs.add(count)
                count = 0
            else:
                count += 1

    return max([*runs])


def parse_file(fname: str) -> Iterable[Robot]:
    with open(fname) as fptr:
        for line in fptr:
            ints = re.findall(r"-{0,1}\d+", line)
            ints = [int(x) for x in ints]
            px, py, vx, vy = ints
            yield (px, py), (vx, vy)


def advance_robot(robot: Robot, w: int, h: int) -> Robot:
    pos, v = robot
    x, y = cartesian_add(pos, v)
    x %= w
    y %= h
    return (x, y), v


def robot_position_after_n(robot: Robot, w: int, h: int, n: int) -> Cartesian:
    pos, v = robot
    pos = cartesian_add_n(pos, v, n)
    x, y = pos
    x %= w
    y %= h
    return x, y


def solve_p1(fname: str, w: int = WIDTH, h: int = HEIGHT) -> int:
    midx = w // 2
    midy = h // 2
    robots = parse_file(fname)
    robots = [robot_position_after_n(robot, w, h, 100) for robot in robots]
    ul = ur = dl = dr = 0
    for x, y in robots:
        if x < midx and y < midy:
            ul += 1
        elif x < midx and y > midy:
            dl += 1
        elif x > midx and y < midy:
            ur += 1
        elif x > midx and y > midy:
            dr += 1

    return ul * ur * dl * dr


def print_state(robots: list[Robot], w: int, h: int) -> None:
    occupied = set([pos for pos, _ in robots])
    for y in range(h):
        for x in range(w):
            if (x, y) in occupied:
                print("0", end=" ")
            else:
                print(" ", end=" ")
        print()


def solve_p2(fname: str) -> None:
    robots = list(parse_file(fname))
    count = 0
    for _ in range(10000):
        robots = [advance_robot(robot, WIDTH, HEIGHT) for robot in robots]
        count += 1

        run = longest_vertical_run(robots, WIDTH, HEIGHT)
        if run > 10:
            print_state(robots, WIDTH, HEIGHT)
            print(count)
            return


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_14.txt", 11, 7), 12)

