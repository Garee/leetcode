#! /usr/bin/env python
"""
Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:

    Input: 121
    Output: true

Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it
    becomes 121-. Therefore it is not a palindrome.

Example 3:

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
import unittest


def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
        return False
    x_str = str(x)
    x_rev_str = x_str[::-1]
    return x_str == x_rev_str


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
