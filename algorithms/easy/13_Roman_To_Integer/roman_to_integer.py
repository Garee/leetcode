#! /usr/bin/env python
"""
Roman numerals are represented by seven different symbols:

    I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

For example, two is written as II in Roman numeral, just two one's added
together. Twelve is written as, XII, which is simply X + II. The number twenty
seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written
as IV. Because the one is before the five we subtract it making four. The same
principle applies to the number nine, which is written as IX. There are six
instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within
the range from 1 to 3999.
"""
import unittest


def roman_to_int(s):
    """
    :type x: str
    :rtype: int
    """
    n = 0
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s)):
        val = vals[s[i]]
        n += val
        if i > 0:
            prev_val = vals[s[i - 1]]
            if prev_val < val:
                n -= prev_val * 2
    return n


class TestSolution(unittest.TestCase):
    def test_example(self):
        s = "III"
        ans = roman_to_int(s)
        self.assertEqual(ans, 3)

    def test_example_2(self):
        s = "IV"
        ans = roman_to_int(s)
        self.assertEqual(ans, 4)

    def test_example_3(self):
        s = "LVIII"
        ans = roman_to_int(s)
        self.assertEqual(ans, 58)

    def test_example_4(self):
        s = "MCMXCIV"
        ans = roman_to_int(s)
        self.assertEqual(ans, 1994)

    def test_min(self):
        s = "I"
        ans = roman_to_int(s)
        self.assertEqual(ans, 1)

    def test_max(self):
        s = "MMMDCCCCLXXXXVIV"
        ans = roman_to_int(s)
        self.assertEqual(ans, 3999)


if __name__ == "__main__":
    unittest.main()
