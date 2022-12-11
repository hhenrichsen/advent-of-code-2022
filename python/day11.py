from functools import reduce
from util import read_stripped_lines

#  ____        _
# |  _ \  __ _| |_ __ _
# | | | |/ _` | __/ _` |
# | |_| | (_| | || (_| |
# |____/ \__,_|\__\__,_|
class Monkey:
    def __init__(self, name, items, op, test, target_true, target_false, factor, div = True):
        self.name = name
        self.items = items
        self.op = op
        self.test = test
        self.target_true = target_true
        self.target_false = target_false
        self.inspected = 0
        self.factor = factor
        self.div = div
        
    def __repr__(self) -> str:
        return f"Monkey {self.name}"
        
    def run(self, monkeys):
        cut = len(self.items)
        for item in self.items:
            self.inspected += 1
            if self.div:
                val = self.op(item) // 3
            else:
                val = self.op(item) % self.factor
            if self.test(val):
                monkeys[self.target_true].items.append(val)
            else:
                monkeys[self.target_false].items.append(val)
        self.items = self.items[cut:]

def parse_operation(line):
    _op, _new, _eq, _old, b, c = list(line.strip().split())
    if b == "+":
        op = lambda a, b: a + b
    elif b == "*":
        op = lambda a, b: a * b
    if c == "old":
        return lambda x: op(x, x)
    else:
        return lambda x: op(x, int(c))

def parse_condition(line):
    ct = line.strip().split()[3]
    ict = int(ct)
    return lambda x: x % ict == 0, ict

def parse_items(line):
    return list(map(int, line.strip().split(":")[1].strip().split(", ")))

def parse_target(line):
    return int(line.strip().split(" ")[5])

def parse_monkey(lines):
    name_str, items_str, operation_str, test_str, t_str, f_str = lines
    name = int(name_str.split()[1][:-1])
    items = parse_items(items_str)
    items2 = parse_items(items_str)
    operation = parse_operation(operation_str)
    test, v = parse_condition(test_str)
    true_target = parse_target(t_str)
    false_target = parse_target(f_str)
    m = Monkey(name, items, operation, test, true_target, false_target, v)
    m2 = Monkey(name, items2, operation, test, true_target, false_target, v)
    monkeys[m.name] = m
    monkeys2[m.name] = m2

#  ____                _
# |  _ \ __ _ _ __ ___(_)_ __   __ _
# | |_) / _` | '__/ __| | '_ \ / _` |
# |  __/ (_| | |  \__ \ | | | | (_| |
# |_|   \__,_|_|  |___/_|_| |_|\__, |
#                              |___/
inp = read_stripped_lines("res/day11.txt")

groups = [[]]
for line in inp:
    if line == "":
        groups.append([])
    else:
        groups[-1].append(line)
        
monkeys = [None] * len(groups)
monkeys2 = [None] * len(groups)

for group in groups:
    parse_monkey(group)

#  ____            _     _
# |  _ \ __ _ _ __| |_  / |
# | |_) / _` | '__| __| | |
# |  __/ (_| | |  | |_  | |
# |_|   \__,_|_|   \__| |_|
#
for i in range(20):
    for monkey in monkeys:
        monkey.run(monkeys)

worst = sorted(monkeys, key = lambda m: m.inspected)[-2:]
print(worst[0].inspected * worst[1].inspected)


#  ____            _      ____
# |  _ \ __ _ _ __| |_   |___ \
# | |_) / _` | '__| __|    __) |
# |  __/ (_| | |  | |_    / __/
# |_|   \__,_|_|   \__|  |_____|
factors = set()
for monkey in monkeys2:
    factors.add(monkey.factor)

f = reduce(lambda a, i: a * i, factors)
for monkey in monkeys2:
    monkey.factor = f
    monkey.div = False

for i in range(10000):
    for monkey in monkeys2:
        monkey.run(monkeys2)
    
worst = sorted(monkeys2, key = lambda m: m.inspected)[-2:]
print(worst[0].inspected * worst[1].inspected)
