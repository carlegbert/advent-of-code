from dataclasses import dataclass
import unittest


FREE = -1


def build_fs(input: str) -> list[int]:
    isfile = True
    id = 0
    result = []
    for c in input.rstrip():
        val = id if isfile else FREE
        result.extend([val] * int(c))
        id += isfile
        isfile = not isfile

    return result


FileSizeAllocation = tuple[
    int,  # size,
    int,  # ID
]


@dataclass
class Block:
    free: int
    files: list[FileSizeAllocation]


def build_block_list(input: str) -> list[Block]:
    isfile = True
    id = 0
    result: list[Block] = []
    for c in input.rstrip():
        size = int(c)
        free = 0 if isfile else size
        files = [(size, id)] if isfile else []
        result.append(Block(free, files))
        id += isfile
        isfile = not isfile

    return result


def non_fragmented_compress(blocks: list[Block]) -> None:
    tailptr = len(blocks)
    free_blocks = [(i, block) for i, block in enumerate(blocks) if block.free > 0]

    while tailptr > 0:
        tailptr -= 1
        block = blocks[tailptr]

        if len(block.files) != 1:
            continue

        for i, free_block in free_blocks:
            if i >= tailptr:
                break

            size, _ = block.files[0]
            if size > free_block.free:
                continue

            free_block.free -= size
            block.free = size
            free_block.files.append(block.files.pop())

            break


def blocks_to_fs(blocks: list[Block]) -> list[int]:
    result: list[int] = []
    for block in blocks:
        for size, id in block.files:
            result.extend([id] * size)
        result.extend([FREE] * block.free)

    return result


def checksum(fs: list[int]) -> int:
    return sum([i * item for i, item in enumerate(fs) if item != FREE])


def compress(fs: list[int]) -> None:
    leftptr, rightptr = 0, len(fs) - 1

    while leftptr < rightptr:
        if fs[leftptr] != FREE:
            leftptr += 1
            continue

        if fs[rightptr] == FREE:
            rightptr -= 1
            continue

        fs[leftptr], fs[rightptr] = fs[rightptr], fs[leftptr]
        leftptr += 1
        rightptr -= 1


def solve_p1(fname: str) -> int:
    fptr = open(fname)
    input = fptr.read()
    fptr.close()

    fs = build_fs(input)
    compress(fs)
    return checksum(fs)


def solve_p2(fname: str) -> int:
    fptr = open(fname)
    input = fptr.read()
    fptr.close()

    blocks = build_block_list(input)
    non_fragmented_compress(blocks)

    fs = blocks_to_fs(blocks)

    return checksum(fs)


class TestCase(unittest.TestCase):
    def test_p1(self):
        self.assertEqual(solve_p1("aoc24/test_inputs/day_09.txt"), 1928)

    def test_p2(self):
        self.assertEqual(solve_p2("aoc24/test_inputs/day_09.txt"), 2858)
