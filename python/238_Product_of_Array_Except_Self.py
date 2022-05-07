"""
238. Product of Array Except Self (Medium)

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Constraints:

   2 <= nums.length <= 105
  -30 <= nums[i] <= 30
  The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List
import unittest


class Solution:

    """
    Patterns: Arrays, Hashing
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)

    Iterate through each num in nums and track each in a num->idx hash map.
    If the matching paired number is already in the hash map, return its index
    and the current index.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        l = 1
        for i, n in enumerate(nums):
            result[i] = l
            l *= n
        r = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= r
            r *= nums[i]
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        ans = self.solution.productExceptSelf(nums)
        assert ans == [24, 12, 8, 6]

    def test_example_2(self):
        nums = [-1, 1, 0, -3, 3]
        ans = self.solution.productExceptSelf(nums)
        assert ans == [0, 0, 9, 0, 0]
