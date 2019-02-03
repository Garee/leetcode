#! /usr/bin/env python
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
"""
import unittest


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def traverse(node, depth=0):
        if node is None:
            return depth
        l_depth = traverse(node.left, depth + 1)
        r_depth = traverse(node.right, depth + 1)
        return max(l_depth, r_depth)

    return traverse(root)


class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class TestSolution(unittest.TestCase):
    def test_example(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        ans = maxDepth(root)
        self.assertEqual(ans, 3)

    def test_empty(self):
        root = None
        ans = maxDepth(root)
        self.assertEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
