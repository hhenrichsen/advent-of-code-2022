from util import (
    parse_grid,
    filter_grid,
    map_grid,
    neighbor_coords,
    flood,
    grid_size,
    breadth_first_search,
)

start = (0, 0)
end = (0, 0)


#  ____                _
# |  _ \ __ _ _ __ ___(_)_ __   __ _
# | |_) / _` | '__/ __| | '_ \ / _` |
# |  __/ (_| | |  \__ \ | | | | (_| |
# |_|   \__,_|_|  |___/_|_| |_|\__, |
#                              |___/
def parse_char(c, x, y):
    global start, end
    if c == "S":
        start = x, y
        return 0
    elif c == "E":
        end = x, y
        return 25
    else:
        return ord(c) - ord("a")


grid = parse_grid("res/day12.txt", parse_char)
directions = map_grid(
    grid,
    lambda item, x, y, grid: [
        (nx, ny) for nx, ny in neighbor_coords(grid, x, y) if grid[ny][nx] <= item + 1
    ],
)


#  ____            _     _
# |  _ \ __ _ _ __| |_  / |
# | |_) / _` | '__| __| | |
# |  __/ (_| | |  | |_  | |
# |_|   \__,_|_|   \__| |_|
#
search = breadth_first_search(
    next=lambda coord: [(x, y) for x, y in directions[coord[1]][coord[0]]],
    found=lambda coord: end == coord,
    serialize=lambda coord: f"{coord[0]}::{coord[1]}",
    optimize_queued=True,
)

_, best, _ = search(start)
print(best)

#  ____            _      ____
# |  _ \ __ _ _ __| |_   |___ \
# | |_) / _` | '__| __|    __) |
# |  __/ (_| | |  | |_    / __/
# |_|   \__,_|_|   \__|  |_____|
          
# Eliminate any start states that are trapped
size = grid_size(grid)
starts = filter_grid(grid, lambda item, x, y: item == 0 and len(directions[y][x]) > 0)
invalid = set()
for start in starts:
    x, y = start
    _, possible = flood(
        grid,
        lambda: True,
        x,
        y,
        next=lambda _, ix, iy: [direction for direction in directions[iy][ix] if direction not in invalid]
    )
    if len(possible) < size:
        if len(list(filter(lambda x: grid[x[1]][x[0]] == 0, possible))) == len(possible):
            invalid = invalid.union(possible)
starts = [start for start in starts if start not in invalid]

# Setup search
search = breadth_first_search(
    next=lambda coord: [(x, y) for x, y in directions[coord[1]][coord[0]]],
    found=lambda coord: end == coord,
    state_filter=lambda coord: coord not in invalid,
    serialize=lambda coord: f"{coord[0]}::{coord[1]}",
    optimize_queued=True,
)

best = None
for start in starts:
    _, res, _ = search(start, best)
    if res is not None and (best is None or res < best):
        best = res

print(best)
