#! /usr/bin/env python
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \\
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \\
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:     1         1
          / \       / \\
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""
import unittest


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p == q:
        return True
    if not haveSameVal(p, q):
        return False
    if not isSameTree(p.left, q.left):
        return False
    if not isSameTree(p.right, q.right):
        return False
    return True


def haveSameVal(p, q):
    if p is None:
        return q is None
    if q is None:
        return p is None
    return p.val == q.val


class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class TestSolution(unittest.TestCase):
    def test_example(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        ans = isSameTree(p, q)
        self.assertTrue(ans)

    def test_example_2(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(3))
        ans = isSameTree(p, q)
        self.assertFalse(ans)

    def test_example_3(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        ans = isSameTree(p, q)
        self.assertFalse(ans)

    def test_none(self):
        p = None
        q = None
        ans = isSameTree(p, q)
        self.assertTrue(ans)

    def test_none_2(self):
        p = None
        q = TreeNode(1, TreeNode(2))
        ans = isSameTree(p, q)
        self.assertFalse(ans)


if __name__ == "__main__":
    unittest.main()
