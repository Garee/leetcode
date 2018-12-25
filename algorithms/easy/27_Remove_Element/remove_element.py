#! /usr/bin/env python
"""
Given an array nums and a value val, remove all instances of that
value in-place and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you
leave beyond the new length.

Example 1:

    Given nums = [3,2,2,3], val = 3,

    Your function should return length = 2, with the first two
    elements of nums being 2.

    It doesn't matter what you leave beyond the returned length.

Example 2:

    Given nums = [0,1,2,2,3,0,4,2], val = 2,

    Your function should return length = 5, with the first five
    elements of nums containing 0, 1, 3, 0, and 4.

    Note that the order of those five elements can be arbitrary.

    It doesn't matter what values are set beyond the returned length.
"""
import unittest


def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    sz = len(nums)
    while sz > 0 and nums[sz - 1] == val:
        sz -= 1
    i = 0
    while i < sz:
        if nums[i] == val:
            nums[i], nums[sz - 1] = nums[sz - 1], nums[i]
            sz -= 1
            while sz > 0 and nums[sz - 1] == val:
                sz -= 1
        i += 1
    return sz


class TestSolution(unittest.TestCase):
    def test_example(self):
        nums = [3, 2, 2, 3]
        val = 3
        ans = remove_element(nums, val)
        self.assertEqual(ans, 2)

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        ans = remove_element(nums, val)
        self.assertEqual(ans, 5)

    def test_empty(self):
        nums = []
        val = 0
        ans = remove_element(nums, val)
        self.assertEqual(ans, 0)

    def test_same_val(self):
        nums = [5, 5, 5, 5, 5, 5, 5, 5]
        val = 5
        ans = remove_element(nums, val)
        self.assertEqual(ans, 0)

    def test_mix(self):
        nums = [2, 3, 5, 2, 4, 8, 5, 3, 2, 5, 9, 9, 5, 6, 7, 3, 5, 2]
        val = 7
        ans = remove_element(nums, val)
        self.assertEqual(ans, 17)

    def test_val_missing(self):
        nums = [1, 2, 3, 4]
        val = 5
        ans = remove_element(nums, val)
        self.assertEqual(ans, 4)

    def test_example_3(self):
        nums = [0, 4, 4, 0, 4, 4, 4, 0, 2]
        val = 4
        ans = remove_element(nums, val)
        self.assertEqual(ans, 4)


if __name__ == "__main__":
    unittest.main()
