from util import read_stripped_lines, sort_lambda

inp = read_stripped_lines("res/day13.txt")
e = list(map(eval, filter(lambda line: len(line) > 0, read_stripped_lines("res/day13.txt"))))
e.append([[2]])
e.append([[6]])

groups = [[]]
for line in inp:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)

pairs = [[eval(item) for item in group] for group in groups]

def compare_item(a, b, spc=0):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return None
        return a < b
    elif isinstance(a, int):  
        a = [a]
    elif isinstance(b, int):
        b = [b]
    for aitem, bitem in zip(a, b):
        if (res := compare_item(aitem, bitem)) is not None:
            return res
    if len(a) < len(b):
        return True
    if len(b) < len(a):
        return False
    return None
    
print(sum(map(lambda x: (x[0] + 1) if (compare_item((x[1][0]), (x[1][1]))) else 0, enumerate(pairs))))

e_s = list(map(str, sort_lambda(e, compare_item)))
print("\n".join(list(map(lambda e: str(e), e_s))))
print((e_s.index("[[2]]") + 1) * (e_s.index("[[6]]") + 1))