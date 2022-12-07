from util import read_stripped_lines

inp = read_stripped_lines("res/day7.txt", "\n")

NAME = 0
PARENT = 1
CHILDREN = 2
SIZE = 3

root = None
current = None 
nodes = []

for line in inp:
    if line.startswith("$"):
        _, cmd, *rest = line.split(" ")
        if cmd == "cd":
            dirname = rest[0]
            if root == None:
                root = [dirname, None, [], 0]
                nodes.append(root)
                current = root
                continue
            if dirname == "..":
                current = current[PARENT]
            else:
                current = list(filter(lambda child: dirname == child[NAME], current[CHILDREN]))[0]
    else:
        size, name = line.split(" ")
        if size == "dir":
            node = [name, current, [], 0]
            current[CHILDREN].append(node)
            nodes.append(node)
        else:
            s = int(size)
            t = current[PARENT]
            while t is not None:
                t[SIZE] += s
                t = t[PARENT]
            current[SIZE] += s

def sum_node(node):
    return node[SIZE]

used = sum_node(root)
target = 30_000_000 - (70_000_000 - used)

print(sum(a[SIZE] for a in filter(lambda node: node[SIZE] < 100000, nodes)))
print(min(a[SIZE] for a in filter(lambda node: node[SIZE] > target, nodes)))