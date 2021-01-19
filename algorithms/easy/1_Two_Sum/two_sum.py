#! /usr/bin/env python
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].

Constraints:

    2 <= nums.length <= 103
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""
import unittest
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    O(n) time as we iterate the list "nums" once.
    O(n) space as we create a dict of len(nums).
    """
    indices = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices:
            j = indices[diff]
            return [j, i]
        indices[n] = i
    return []


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = two_sum(nums, target)
        self.assertEqual(ans, [0, 1])

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        ans = two_sum(nums, target)
        self.assertEqual(ans, [1, 2])

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        ans = two_sum(nums, target)
        self.assertEqual(ans, [0, 1])


if __name__ == "__main__":
    unittest.main()
