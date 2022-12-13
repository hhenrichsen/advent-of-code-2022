from typing import Iterable, List, TypeVar
from numbers import Number


A = TypeVar("A")
B = TypeVar("B")


def read_stripped_lines(path: str, chars: str = "\n") -> List[str]:
    with open(path) as f:
        return list(map(lambda line: line.strip(chars), f.readlines()))


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


def windows(l, sz):
    return [l[i - sz : i] for i in range(sz, len(l) + 1)]

def sort_lambda(l, fn):
    class __InternalSort:
        def __init__(self, v):
            self.v = v
            
        def __lt__(self, other):
            res = fn(self.v, other.v)
            if isinstance(res, bool):
                return res 
            elif isinstance(res, Number):
                return res < 0
        
    c_list = list(map(__InternalSort, l))
    return list(map(lambda c: c.v, sorted(c_list)))

    
