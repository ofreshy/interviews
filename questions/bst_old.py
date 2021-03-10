# TODO 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print self.value


class Tree(object):
    def __init__(self):
        self.root = None

    def depth_first(self):
        pass

    def breadth_first(self):
        pass

    def get(self, value):
        def _search(node):
            if node is None:
                return False
            elif node.value == value:
                return True
            elif value < node.value:
                return _search(node.left)
            else:
                return _search(node.right)
        return _search(self.root)

    def get2(self, value):
        n = self.root
        while n is not None:
            if n.value == value:
                return True
            elif value < n.value:
                n = n.left
            elif value > n.value:
                n = n.right
        return False

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, parent, value):
        n_value = parent.value
        if value < n_value:
            if parent.left is None:
                parent.left = Node(value)
            else:
                self._insert(parent.left, value)
        else:
            if parent.right is None:
                parent.right = Node(value)
            else:
                self._insert(parent.right, value)

    def put(self, value):
        self.root = self._put(self.root, value)

    def _put(self, node, value):
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._put(node.left, value)
        else:
            node.right = self._put(node.right, value)
        return node


    def __repr__(self):
        node = self.root


t = Tree()
t.insert(5)
t.insert(10)
t.insert(7)
print t.get(5)
print t.get(10)
print t.get(19)

print t.get2(5)
print t.get2(10)
print t.get2(19)

t.put(15)
t.put(110)
t.put(17)

print t.get(15)
print t.get(110)
print t.get(117)

