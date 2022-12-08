from util import read_stripped_lines

inp = read_stripped_lines("res/day8.txt", "\n")

grid = []
for line in inp:
    grid.append(list(map(int, list(line))))

count = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        item = grid[y][x]
        if (
            len([grid[ym][x] for ym in range(0, y) if grid[ym][x] >= item]) == 0
            or len([grid[y][xm] for xm in range(0, x) if grid[y][xm] >= item]) == 0
            or len([grid[y][xm] for xm in range(x + 1, len(grid[y])) if grid[y][xm] >= item]) == 0
            or len([grid[ym][x] for ym in range(y + 1, len(grid)) if grid[ym][x] >= item]) == 0
        ):
            count += 1


def find_list_score(ls, mx):
    ct = 0
    for item in ls:
        ct += 1
        if item >= mx:
            break
    return ct


def find_scenic_score(grid, x, y):
    v = grid[y][x]
    return (
        (find_list_score(([grid[ym][x] for ym in range(y - 1, -1, -1)]), v))
        * (find_list_score(([grid[y][xm] for xm in range(x - 1, -1, -1)]), v))
        * (find_list_score(([grid[y][xm] for xm in range(x + 1, len(grid[y]))]), v))
        * (find_list_score(([grid[ym][x] for ym in range(y + 1, len(grid))]), v))
    )


count = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        item = grid[y][x]
        if (
            len([grid[ym][x] for ym in range(0, y) if grid[ym][x] >= item]) == 0
            or len([grid[y][xm] for xm in range(0, x) if grid[y][xm] >= item]) == 0
            or len([grid[y][xm] for xm in range(x + 1, len(grid[y])) if grid[y][xm] >= item]) == 0
            or len([grid[ym][x] for ym in range(y + 1, len(grid)) if grid[ym][x] >= item]) == 0
        ):
            count += 1

mx = 0
for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
        score = find_scenic_score(grid, x, y)
        if score > mx:
            mx = score

print(count)
print(mx)
