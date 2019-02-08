#! /usr/bin/env python
"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
import unittest


def moveZeroes(nums: "List[int]") -> "None":
    n = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[n], nums[i] = nums[i], nums[n]
            n += 1


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [0, 1, 0, 3, 12]
        moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_empty(self):
        nums = []
        moveZeroes(nums)
        self.assertEqual(nums, [])

    def test_zeros(self):
        nums = [0, 0, 0, 0, 0, 0]
        moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
