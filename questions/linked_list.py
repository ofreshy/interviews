
class Node(object):
    def __init__(self, value):
        self.value = value
        self.nxt = None


class LinkedList(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            prev = self._get_node(self.size - 1)
            prev.nxt = node
        self.size += 1

    def delete(self, index):
        if index > self.size:
            raise
        if index == 0:
            removed = self.root
            self.root = None
        else:
            prev = self._get_node(index-1)
            removed = prev.nxt
            prev.nxt = removed.nxt

        self.size -= 1
        return removed

    def _get_node(self, n):
        node = self.root
        for i in xrange(n):
            node = node.nxt
        return node

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if self.size <= index:
            raise IndexError("too big")
        node = self._get_node(index)
        return node.value

    def __repr__(self):
        st = ""
        node = self.root
        while node is not None:
            st += "%s," % node.value
            node = node.nxt
        st = st[:-1]
        return "[" + st + "]"

    def __iter__(self):
        pass

l = LinkedList()
assert len(l) == 0
print l
l.insert(0)
assert len(l) == 1
print l

l.insert(2)
assert len(l) == 2

assert l[0] == 0
assert l[1] == 2
print l
l.delete(1)
l.delete(0)
print l
