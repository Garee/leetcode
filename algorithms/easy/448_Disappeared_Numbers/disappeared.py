#! /usr/bin/env python
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
import unittest


def findDisappearedNumbers(nums: "List[int]") -> "List[int]":
    appear = {n: True for i, n in enumerate(nums)}
    missing = []
    for i in range(1, len(nums) + 1):
        if i not in appear:
            missing.append(i)
    return missing


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        ans = findDisappearedNumbers(nums)
        self.assertEqual(ans, [5, 6])

    def test_example_2(self):
        nums = [1, 1]
        ans = findDisappearedNumbers(nums)
        self.assertEqual(ans, [2])


if __name__ == "__main__":
    unittest.main()
