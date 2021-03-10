# -*- coding: utf-8 -*-

"""
A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.
"""


class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def is_leaf(self):
        return (self.left, self.right) is (None, None)


def is_super_balanced(root):
    try:
        walk_tree(root, 0, [], [])
    except AssertionError:
        return False
    else:
        return True


def is_super_balanced(node):
    min_depth, max_depth = [], []

    def check(node, depth):
        if not node:
            return

        if node.is_leaf():
            if not min_depth:
                min_depth.append(depth)
            else:
                min_depth[0] = min(depth, min_depth[0])
            if not max_depth:
                max_depth.append(depth)
            else:
                max_depth[0] = max(depth, max_depth[0])

            if max_depth[0] - min_depth[0] > 1:
                raise AssertionError("Found it")

        check(node.left, depth+1)
        check(node.right, depth+1)

    try:
        check(node, 0)
        return True
    except AssertionError:
        return False


def walk_tree(node, cur_depth, min_depth, max_depth):
    if node is None:
        return
    if node.is_leaf():
        if not min_depth:
            min_depth.append(cur_depth)
        else:
            min_depth[0] = min(min_depth[0], cur_depth)
        if not max_depth:
            max_depth.append(cur_depth)
        else:
            max_depth[0] = max(max_depth[0], cur_depth)

        if max_depth[0] - min_depth[0] > 1:
            raise AssertionError
    walk_tree(node.left, cur_depth+1, min_depth, max_depth)
    walk_tree(node.right, cur_depth+1, min_depth, max_depth)


r = BinaryTreeNode(0)
assert is_super_balanced(r)

r.left = BinaryTreeNode(1)
r.right = BinaryTreeNode(2)
assert is_super_balanced(r)

r.left.left = BinaryTreeNode(3)
assert is_super_balanced(r)

r.left.left.left = BinaryTreeNode(3)
assert is_super_balanced(r) is False





