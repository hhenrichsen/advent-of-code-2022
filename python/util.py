from typing import Iterable, List, TypeVar


A = TypeVar("A")


def read_stripped_lines(path: str) -> List[str]:
    with open(path) as f:
        return list(map(lambda line: line.strip(), f.readlines()))


def partition_list(list: Iterable[A], count: int) -> List[List[A]]:
    """
    Assumes len(list) % count == 0

    Split a list into `count` parts.
    """
    part_len = len(list) // count
    return [list[i : i + part_len] for i in range(0, len(list), part_len)]


def intersect_strings(strings):
    init = set(list(strings[0]))
    for other in strings[1:]:
        init = init.intersection(list(other))
    return list(init)
