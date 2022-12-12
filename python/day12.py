from util import parse_grid, filter_grid, map_grid, neighbor_coords

start = (0, 0)
end = (0, 0)
def parse_char(c, x, y):
    global start, end
    if c == "S":
        start = x, y
        return 0
    elif c == "E":
        end = x, y
        return 25
    else:
        return ord(c) - ord('a')

grid = parse_grid("res/day12a.txt", parse_char)
directions = map_grid(grid, lambda item, x, y, grid: [(nx, ny) for nx, ny in neighbor_coords(grid, x, y) if grid[ny][nx] <= item + 1])

def search(start, limit = None):
    q = [(0, start)]
    visited = set()
    queued = set()
    while len(q) > 0:
        state = q.pop(0)

        ln, coord = state
        if limit is not None and ln > limit:
            return None
        sx, sy = coord
        visited.add(f"{sx}::{sy}")

        next_states = [(ln + 1, (x, y)) for x, y in directions[sy][sx] if f"{x}::{y}" not in visited and f"{x}::{y}" not in queued]
        for next_state in next_states:
            nln, ncoord = next_state
            nx, ny = ncoord
            if ncoord == end:
                return nln
            q.append(next_state)
            queued.add(f"{nx}::{ny}")

print(search(start))

starts = filter_grid(grid, lambda item, x, y: item == 0 and len(directions[y][x]) > 0)
best = None
for start in starts:
    res = search(start, best)
    if res is not None and best is None or res < best:
        best = res
    
print(best)