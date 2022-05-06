"""
217. Contains Duplicate (Easy)

Given an integer array nums, return true if any value appears at least twice
in the array, and return false if every element is distinct.

Constraints:

  1 <= nums.length <= 105
  -109 <= nums[i] <= 109
"""
from typing import List
import unittest


class Solution:

    """
    Patterns: Arrays, Sets
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)

    Iterate through nums and track which nums have already been
    met in a set. At each number, if it is already in the set it
    is a duplicate, therefore return true.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 1]
        ans = self.solution.containsDuplicate(nums)
        assert ans

    def test_example_2(self):
        nums = [1, 2, 3, 4]
        ans = self.solution.containsDuplicate(nums)
        assert not ans
