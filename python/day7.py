from util import read_stripped_lines

inp = read_stripped_lines("res/day7.txt", "\n")

DIR = 0
NAME = 1
PARENT = 2
CHILDREN = 3

root = None
current = None 
last_spaces = -1

for line in inp:
    if line.startswith("$"):
        _, cmd, *rest = line.split(" ")
        if cmd == "cd":
            dirname = rest[0]
            if root == None:
                root = (True, dirname, None, [])
                current = root
                continue
            if dirname == "..":
                current = current[PARENT]
            else:
                current = list(filter(lambda child: dirname == child[NAME], current[CHILDREN]))[0]
    else:
        size, name = line.split(" ")
        if size == "dir":
            current[CHILDREN].append((True, name, current, []))
        else:
            current[CHILDREN].append((False, name, current, int(size)))
        
def nodes_of_size(root, sz):
    nodes = []
    def sum_node(node):
        if isinstance(node[CHILDREN], int):
            return node[CHILDREN]
        else:
            sm = sum(sum_node(x) for x in node[CHILDREN])
            if sm < sz:
                nodes.append((sm, node))
            return sm
    sum_node(root)
    return nodes
        
def nodes_gt_size(root, sz):
    nodes = []
    def sum_node(node):
        if isinstance(node[CHILDREN], int):
            return node[CHILDREN]
        else:
            sm = sum(sum_node(x) for x in node[CHILDREN])
            if sm > sz:
                nodes.append((sm, node))
            return sm
    sum_node(root)
    return nodes

def sum_node(node):
    if isinstance(node[CHILDREN], int):
        return node[CHILDREN]
    else:
        return sum(sum_node(x) for x in node[CHILDREN])

total = 70_000_000 
reqd = 30_000_000
used = sum_node(root)
current = total - used
target = reqd - current

print(sum(a[0] for a in nodes_of_size(root, 100000)))
print(min(a[0] for a in nodes_gt_size(root, target)))