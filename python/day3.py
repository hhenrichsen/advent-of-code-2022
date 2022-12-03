from functools import reduce

from util import partition_list, intersect_strings


def priority(c: str):
    if c.isupper():
        return (ord(c) - ord("A")) + 27
    else:
        return (ord(c) - ord("a")) + 1


def get_shared_char_from_halves(s: str):
    return intersect_strings(partition_list(list(s), 2))[0]


def part1(inp):
    return reduce(
        lambda current, line: current + priority(get_shared_char_from_halves(line)),
        inp,
        0,
    )


def part2(inp):
    return reduce(
        lambda current, chunk: current + priority(intersect_strings(chunk)[0]),
        [inp[i : i + 3] for i in range(0, len(inp), 3)],
        0,
    )


inp = None
with open("res/day3.txt") as f:
    inp = list(map(lambda s: s.strip(), f.readlines()))


print(part1(inp))
print(part2(inp))
