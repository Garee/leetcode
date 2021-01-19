#! /usr/bin/env python
"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

Example 1:

    Input: x = 121
    Output: true

Example 2:

    Input: x = -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: x = 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

    Input: x = -101
    Output: false


Constraints:

    -231 <= x <= 231 - 1
"""
import unittest


def is_palindrome(x: int) -> bool:
    """
    O(1) time and space.
    """
    x_str = str(x)
    return x_str == x_str[::-1]


class TestSolution(unittest.TestCase):
    def test_example(self):
        x = 121
        ans = is_palindrome(x)
        self.assertTrue(ans)

    def test_neg(self):
        x = -121
        ans = is_palindrome(x)
        self.assertFalse(ans)

    def test_zero(self):
        x = 10
        ans = is_palindrome(x)
        self.assertFalse(ans)


if __name__ == "__main__":
    unittest.main()
