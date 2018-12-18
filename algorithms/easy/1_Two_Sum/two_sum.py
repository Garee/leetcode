#! /usr/bin/env python
"""
Given an array of integers, return indices of the two numbers such that
they add up to a specific target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
import unittest


def two_sum(nums, target):
    """
    O(n) time, O(1) space

    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    partners = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in partners:
            j = partners[diff]
            return [i, j]
        partners[n] = i
    return []


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = two_sum(nums, target)
        self.assertEqual(ans, [1, 0])


if __name__ == "__main__":
    unittest.main()
