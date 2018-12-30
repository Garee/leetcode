#! /usr/bin/env python
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:

    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:

    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

"""
import unittest


def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack) - len(needle) + 1):
        s = haystack[i: i + len(needle)]
        print(s, needle, i)
        if s == needle:
            return i
    return -1


class TestSolution(unittest.TestCase):
    def test_example(self):
        haystack = "hello"
        needle = "ll"
        ans = str_str(haystack, needle)
        self.assertEqual(ans, 2)

    def test_example_2(self):
        haystack = "aaaaa"
        needle = "bba"
        ans = str_str(haystack, needle)
        self.assertEqual(ans, -1)

    def test_empty(self):
        haystack = "haystack"
        needle = ""
        ans = str_str(haystack, needle)
        self.assertEqual(ans, 0)

    def test_not_found(self):
        haystack = "haystack"
        needle = "blah"
        ans = str_str(haystack, needle)
        self.assertEqual(ans, -1)

    def test_single_letter(self):
        haystack = "a"
        needle = "a"
        ans = str_str(haystack, needle)
        self.assertEqual(ans, 0)


if __name__ == "__main__":
    unittest.main()
