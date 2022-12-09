from util import ilp, l, read_stripped_lines, windows
from math import copysign

inp = read_stripped_lines("res/day9.txt", "\n")

direction = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail
    dx = hx - tx
    adx = abs(dx)
    dy = hy - ty
    ady = abs(dy)
    if dx == 0 and ady == 2:
        return (0, copysign(1, dy))
    elif dy == 0 and adx == 2:
        return (copysign(1, dx), 0)
    elif adx == 2 or ady == 2:
        return (copysign(1, dx), copysign(1, dy))
    else:
        return (0, 0)
    
for ct in [2, 10]:
    visited = set()
    knots = []
    for i in range(ct):
        knots.append((0, 0))
        
    for line in inp:
        dirsym, count = list(line.split())
        dx, dy = direction[dirsym]
        for _ in range(int(count)):
            # Move head
            hx, hy = knots[0]
            knots[0] = (hx + dx, hy + dy)
            # Resolve tails
            for idx in range(1, len(knots)):
                head = knots[idx-1]
                tail = knots[idx]
                # print("Head: ", head)
                # print("Tail: ", tail, end=" --")
                tdx, tdy = move_tail(head, tail)
                # print(f"({tdx}, {tdy})", end="-> ")
                tx, ty = tail
                tail = tx + tdx, ty + tdy
                knots[idx] = tail
                # print(tail)
                ntx, nty = tail
            # Mark tail visited
            ntx, nty = knots[-1]
            visited.add(f"{int(ntx)}::{int(nty)}")
            
    print(len(visited))
