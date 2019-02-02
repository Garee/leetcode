#! /usr/bin/env python
"""
Given a non-empty array of integers, every element appears twice except for
one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
import unittest


def singleNumber(nums):
    n = 0
    for num in nums:
        n ^= num
    return n


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [2, 2, 1]
        ans = singleNumber(nums)
        self.assertEqual(ans, 1)

    def test_example_2(self):
        nums = [4, 1, 2, 1, 2]
        ans = singleNumber(nums)
        self.assertEqual(ans, 4)

    def test_example_3(self):
        nums = [-1, -1, 2]
        ans = singleNumber(nums)
        self.assertEqual(ans, 2)


if __name__ == "__main__":
    unittest.main()
