from util import read_stripped_lines
import re

inp = read_stripped_lines("res/day5.txt", "\n")

stacks = []
stacks2 = []
instructions = []

stack_mode = True
for line in inp:
    if line == "":
        stack_mode = False
        stacks = list(
            map(lambda x: x[:-1], stacks)
        )  # remove stack numbers, we don't need them
        continue
    if stack_mode:
        parts = [line[i + 1] for i in range(0, len(line), 4)]
        for idx, item in enumerate(parts):
            if len(stacks) == 0:
                for _ in range(len(parts)):
                    stacks.append([])
                    stacks2.append([])
            if item != " ":
                stacks[idx].append(item)
                stacks2[idx].append(item)
    else:
        instructions.append(list(map(int, re.findall(r"\d+", line))))

for instruction in instructions:
    count, source, dest = instruction

    # Part 1
    items = stacks[source - 1][:count]
    stacks[source - 1] = stacks[source - 1][count:]
    for item in items:
        stacks[dest - 1].insert(0, item)

    # Part 2
    items2 = stacks2[source - 1][:count]
    stacks2[source - 1] = stacks2[source - 1][count:]
    for item in items2[::-1]:
        stacks2[dest - 1].insert(0, item)

print("".join(map(lambda s: s[0] if len(s) > 0 else "", stacks)))
print("".join(map(lambda s: s[0] if len(s) > 0 else "", stacks2)))
