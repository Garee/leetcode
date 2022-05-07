"""
374. Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most
frequent elements. You may return the answer in any order.

Constraints:

  1 <= nums.length <= 105
  k is in the range [1, the number of unique elements in the array].
  It is guaranteed that the answer is unique.
"""
from typing import List
import unittest


class Solution:

    """
    Patterns: Arrays, Hashing
    Time: O(n) where n is len(nums)
    Space: O(n) where n is len(nums)

    Iterate through each num and count the frequency of occurences
    in a hash map. Get an array of unique nums and sort it by
    frequency in ascending order. Take the first k elements from
    this array as the result.
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        uniq_nums = list(counts.keys())
        sorted_nums = sorted(uniq_nums, key=lambda x: counts[x], reverse=True)
        return sorted_nums[:k]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        ans = self.solution.topKFrequent(nums, k)
        assert ans == [1, 2]

    def test_example_2(self):
        nums = [1]
        k = 1
        ans = self.solution.topKFrequent(nums, k)
        assert ans == [1]
