#! /usr/bin/env python
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

    Input: 123
    Output: 321

Example 2:

    Input: -123
    Output: -321

Example 3:

    Input: 120
    Output: 21

Note:
Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose
of this problem, assume that your function returns 0 when the reversed
integer overflows.
"""
import unittest


def reverse(x):
    """
    O(n) time, O(n) space

    :type x: int
    :rtype: int
    """
    x_str = str(x)
    x_rev_str = x_str[::-1]
    if x_rev_str[-1] == "-":
        x = -int(x_rev_str[:-1])
    else:
        x = int(x_rev_str)
    if x < -2 ** 31 or x > 2 ** 31 - 1:
        return 0
    return x


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
