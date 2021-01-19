#! /usr/bin/env python
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

    Input: x = 123
    Output: 321

Example 2:

    Input: x = -123
    Output: -321

Example 3:

    Input: x = 120
    Output: 21

Example 4:

    Input: x = 0
    Output: 0

Constraints:

    -231 <= x <= 231 - 1
"""
import unittest


def reverse(x: int) -> int:
    """
    O(n) time and O(n) space as we reverse the integer string.
    """
    x_str = str(x)
    is_neg = x_str[0] == "-"
    rev_s = x_str[::-1]
    rev = -int(rev_s[:-1]) if is_neg else int(rev_s)
    if rev < -(2 ** 31) or rev > (2 ** 31 - 1):
        return 0
    return rev


class TestSolution(unittest.TestCase):
    def test_example(self):
        x = 123
        ans = reverse(x)
        self.assertEqual(ans, 321)

    def test_neg(self):
        x = -123
        ans = reverse(x)
        self.assertEqual(ans, -321)

    def test_zero(self):
        x = 120
        ans = reverse(x)
        self.assertEqual(ans, 21)

    def test_many_zeros(self):
        x = 100000
        ans = reverse(x)
        self.assertEqual(ans, 1)

    def test_overflow(self):
        x = 4294967294
        ans = reverse(x)
        self.assertEqual(ans, 0)

    def test_neg_overflow(self):
        x = -4294967294
        ans = reverse(x)
        self.assertEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
