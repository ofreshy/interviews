
class UnionFind(object):
    def __init__(self):
        self.con = [set([x]) for x in xrange(10)]

    def union(self, a, b):
        for x in self.con[b]:
            self.con[a].add(x)
        self.con[b] = self.con[a]

    def find(self, a, b):
        return b in self.con[a]


uf = UnionFind()

uf.union(1, 9)
assert uf.find(1, 9)

uf.union(2, 8)
assert uf.find(2, 8)
assert not uf.find(1, 8)
assert not uf.find(1, 2)
assert not uf.find(9, 8)

uf.union(8, 4)
assert uf.find(4, 2)
assert uf.find(2, 4)
