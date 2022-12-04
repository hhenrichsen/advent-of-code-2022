from util import read_stripped_lines

inp = read_stripped_lines("res/day4.txt")

def part1(lines):
    count = 0
    for line in lines:
        a, b = line.split(",")
        a_low, a_high = list(map(int, a.split("-")))
        b_low, b_high = list(map(int, b.split("-")))
        if a_low >= b_low and a_high <= b_high:
            count += 1
        elif b_low >= a_low and b_high <= a_high:
            count += 1
            
    return count

def part2(lines):
    count = 0
    for line in lines:
        a, b = line.split(",")
        a_low, a_high = list(map(int, a.split("-")))
        b_low, b_high = list(map(int, b.split("-")))
        set_a = set(range(a_low, a_high+1))
        set_b = set(range(b_low, b_high+1))
        overlap = set_a.intersection(set_b)
        if len(overlap) > 0:
            count += 1
            
    return count


print(part1(inp))
print(part2(inp))
