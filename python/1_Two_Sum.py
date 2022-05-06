"""
1. Two Sum (Easy)

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Constraints:

  2 <= nums.length <= 104
  -109 <= nums[i] <= 109
  -109 <= target <= 109
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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        met = {}
        for i, n in enumerate(nums):
            need = target - n
            if need in met:
                return [met[need], i]
            met[n] = i
        return []


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        ans = self.solution.twoSum(nums, target)
        assert ans == [0, 1]

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        ans = self.solution.twoSum(nums, target)
        assert ans == [1, 2]

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        ans = self.solution.twoSum(nums, target)
        assert ans == [0, 1]


if __name__ == "__main__":
    unittest.main()
