"""
Given the sequence of elements count the number of elements
 H2O = {H:2, O:1}
 O[Na[G]3]3 = {O:1, Na:3, G:9}
 
 Rules :
 Expression may start with [ or capital letter
 After Capital letter - expect lower or Another Capital or a digit or [ or ]
 After lower expect digit or Upper or Number or [
 After Digit expect digit lower upper [ ]
 After [ expect Capital 
 After ] expect digit
"""


def parse(expr):
    state = "new"
    token, rest = read_new(expr)

def read_new(expr):
    t = expr[0]
    if t.is_alpha() and t.upper() == t:
        j = 1
        n = expr[j]


from collections import Counter


def mult_counter(value, c):
    return Counter({k: v*value for k, v in c.items()})


def to_counter(nodes):
    c = Counter()
    for node in nodes:
        v = node.value
        if v.isalpha():
            c[v] += 1
        else:
            c += mult_counter(int(v), to_counter(node.children))
    return c


class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []

    def is_leaf(self):
        return not bool(self.children)


def count_elements(sequence):
    elem = []
    for i in xrange(len(sequence)):
        e = sequence[i]


a = Node("3")
a.children.append(Node("F"))
a.children.append(Node("B"))
a.children.append(Node("HO"))

assert Counter({'B': 3, 'HO': 3, 'F': 3}) == to_counter([a])

b = Node("5")
b.children.append(Node("G"))
a.children.append(b)

assert Counter({'G': 15, 'B': 3, 'HO': 3, 'F': 3}) == to_counter([a])

