from functools import reduce
from util import read_stripped_lines

inp = read_stripped_lines("res/day10.txt", "\n")
targets = [20, 60, 100, 140, 180, 220]
results = []

counter = 0
registers = {
    'x': 1
}
def check_count():
    if counter in targets:
        print(registers["x"])
        results.append(counter * registers["x"])

for instruction in inp:
    parts = instruction.split(" ")
    if parts[0] == "noop":
        counter += 1
        check_count()
    else:
        counter += 1
        check_count()
        counter += 1
        registers["x"] += int(parts[1])
        check_count()
    
counter = 0
register = 1
def check_count2():
    ctmod = counter % 40
    if register in range(ctmod-1, ctmod+2):
        print("#", end="")
    else:
        print(".", end="")
    if ctmod == 0:
        print()

for instruction in inp:
    parts = instruction.split(" ")
    if parts[0] == "noop":
        counter += 1
        check_count2()
    else:
        counter += 1
        check_count2()
        counter += 1
        register += int(parts[1])
        check_count2()
