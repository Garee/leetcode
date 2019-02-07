#! /usr/bin/env python
"""
Given an n-ary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""
import unittest


def levelOrder(root: "Node") -> "List[List[int]]":
    return traverse(root, [])


def traverse(node, order, level=0):
    if node is None:
        return []
    if len(order) < level + 1:
        order.append([])
    order[level].append(node.val)
    for c in node.children:
        traverse(c, order, level + 1)
    return order


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children


class TestSolution(unittest.TestCase):
    def test_example(self):
        node = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
        ans = levelOrder(node)
        self.assertEqual(ans, [[1], [3, 2, 4], [5, 6]])


if __name__ == "__main__":
    unittest.main()
