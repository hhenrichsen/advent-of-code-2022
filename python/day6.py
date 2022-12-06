from util import read_stripped_lines

inp = read_stripped_lines("res/day6.txt", "\n")

for idx in range(4, len(inp[0])):
    chrs = set(list(inp[0][idx-4:idx]))
    if len(chrs) == 4:
        print(idx)
        break

for idx in range(14, len(inp[0])):
    chrs = set(list(inp[0][idx-14:idx]))
    if len(chrs) == 14:
        print(idx)
        break
