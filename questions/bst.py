
class _Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        print "<Node : key=key, value=value>".format(
            key=self.key, value=self.value
        )


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __getitem__(self, key):
        def _get(node):
            if node is None:
                raise KeyError("%s is not in tree" % key)
            if node.key == key:
                return node.value
            elif key < node.key:
                return _get(node.left)
            else:
                return _get(node.right)
        return _get(self.root)

    def __setitem__(self, key, value):
        def _put(node):
            if node is None:
                return _Node(key=key, value=value)
            if key == node.key:
                node.value = value
            elif key < node.key:
                node.left = _put(node.left)
            else:  # key > node.left:
                node.right = _put(node.right)
            return node
        self.root = _put(self.root)

    def traverse_depth_first(self):
        heap = [self.root]
        while heap:
            n = heap.pop()
            if n.left:
                heap = [n.left] + heap
            if n.right:
                heap = [n.right] + heap
            yield n

    def traverse_breadth_first(self):
        heap = [self.root]
        while heap:
            n = heap.pop()
            yield n
            if n.left:
                heap += [n.left]
            if n.right:
                heap += [n.right]

t = BinarySearchTree()

t[1] = 11
t[2] = 12
t[3] = 13
t[4] = 12
t[1] = 15
t[-1] = 10
print t


assert t[1] == 15
assert t[2] == 12
assert t[3] == 13
assert t[4] == 12


assert 4 in t
assert 2 in t
assert 3 in t
assert 1 in t

assert 5 not in t


def depth_first(tree):
    def print_node(n):
        if n is None:
            return
        print n.key, n.value
        print_node(n.left)
        print_node(n.right)
    print_node(tree.root)


def breadth_first(tree):
    q = [tree.root] if tree.root else []

    def print_node():
        if not q:
            return
        n = q.pop(0)
        print n.key, n.value
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)

        print_node()

    print_node()



s = BinarySearchTree()

s[5] = 10
s[3] = 3
s[1] = 6
s[10] = 15
depth_first(s)
print
breadth_first(s)

print ("---")
for n in s.traverse_depth_first():
    print n.value

print ("---")
for n in s.traverse_breadth_first():
    print n.value
