from util import read_stripped_lines
from itertools import tee

inp = read_stripped_lines("res/day14.txt")

filled = set()
source = (500, 0)
maxy = 0

for line in inp:
    pairs = line.split("->")
    a, b = tee(pairs)
    next(b, None)
    pairs = zip(a, b)
    for a, b in pairs:
        ax, ay = list(map(int, list(a.split(","))))
        bx, by = list(map(int, list(b.split(","))))
        for x in range(min(ax, bx), max(ax, bx) + 1):
            for y in range(min(ay, by), max(ay, by) + 1):
                filled.add((x, y))
                maxy = max(maxy, y)
                
maxy += 1
print("Max", maxy)
                
ct = 0
blocked_a = set()

def is_blocked(x, y):
    return (x, y) in filled or (x, y) in blocked_a

fall = lambda s: (s[0], s[1] + 1)

cont = True
while cont:
    sand = source
    while cont:
        while not is_blocked(*fall(sand)):
            sand = fall(sand)
            _, sy = sand
            if sy > maxy:
                cont = False
                break
        sx, sy = sand
        if not is_blocked(sx-1, sy+1):
            sand = (sx-1, sy+1)
        elif not is_blocked(sx+1, sy+1):
            sand = (sx+1, sy+1)
        else:
            ct += 1
            blocked_a.add(sand)
            break


print(ct)

maxy += 1
def is_blocked_b(x, y):
    return (x, y) in filled or (x, y) in blocked_b or y >= maxy

blocked_b = set()
ct = 0
cont = True
while cont:
    if is_blocked_b(*source):
        break
    sand = source
    while cont:
        while not is_blocked_b(*fall(sand)):
            sand = fall(sand)
            _, sy = sand
        sx, sy = sand
        if not is_blocked_b(sx-1, sy+1):
            sand = (sx-1, sy+1)
        elif not is_blocked_b(sx+1, sy+1):
            sand = (sx+1, sy+1)
        else:
            ct += 1
            blocked_b.add(sand)
            break

print(ct)