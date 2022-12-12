from inspect import signature
from typing import Callable, List, Tuple, TypeVar
from .util import read_stripped_lines


A = TypeVar("A")
B = TypeVar("B")

GridCall = Callable[[A, int, int, List[List[A]]], B]
GridCallCandidate = (
    Callable[[], B]
    | Callable[[A], B]
    | Callable[[A, List[List[A]]], B]
    | Callable[[A, int, int], B]
    | GridCall
)

AGrid = List[List[A]]
BGrid = List[List[B]]
Coord = Tuple[int, int]


def neighbor_coords(grid: AGrid, x: int, y: int) -> List[Coord]:
    """
    Get a list of valid neighbor coordinates
    """
    res = []
    if y < len(grid) and len(grid[y]) > x + 1:
        res.append((x + 1, y))
    if y < len(grid) and x - 1 >= 0:
        res.append((x - 1, y))
    if y + 1 < len(grid) and x < len(grid[y]):
        res.append((x, y + 1))
    if y - 1 >= 0:
        res.append((x, y - 1))
    return res


def grid_call(fn: GridCallCandidate, name: str) -> GridCall:
    """
    Figures out how many parameters a grid function parameter is expecting and
    returns a function that uses that many parameters while handling the four
    that one of the grid functions is expecting.
    """
    sig = signature(fn)
    ct = len(sig.parameters)
    if ct == 0:
        return lambda _item, _x, _y, _grid: fn()
    elif ct == 1:
        return lambda item, _x, _y, _grid: fn(item)
    elif ct == 2:
        return lambda item, _x, _y, grid: fn(item, grid)
    elif ct == 3:
        return lambda item, x, y, _: fn(item, x, y)
    elif ct == 4:
        return fn
    else:
        raise Exception(
            f"Invalid function reference param number {ct} for grid function {name}"
        )


def parse_grid(
    filename: str,
    item_parser: Callable[[A], B],
    line_splitter: Callable[[List[str]], List[A]] = lambda line: list(line),
) -> BGrid:
    """
    Parses a text file into a grid using the given item parser. Defaults to
    splitting lines character-wise.
    """
    inp = read_stripped_lines(filename)
    grid = []
    for y, line in enumerate(map(line_splitter, inp)):
        grid.append([])
        for x, item in enumerate(line):
            grid[-1].append(item_parser(item, x=x, y=y))
    return grid


def filter_grid(grid: AGrid, filter: GridCallCandidate) -> List[Coord]:
    """
    Finds coordinates where a given filter returns true in a grid.
    """
    fn = grid_call(filter, "filter_grid")
    results = []
    for y, row in enumerate(grid):
        for x, item in enumerate(row):
            if fn(item, x, y, grid):
                results.append((x, y))
    return results


def map_grid(grid: AGrid, map: GridCallCandidate) -> BGrid:
    """
    Transforms each item in a grid to something else.
    """
    fn = grid_call(map, "map_grid")
    results = []
    for y, row in enumerate(grid):
        results.append([])
        for x, item in enumerate(row):
            results[-1].append(fn(item, x, y, grid))
    return results
