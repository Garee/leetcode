#! /usr/bin/env python
"""
Write a function to find the longest common prefix string amongst an
array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""
import unittest


def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    s = strs[0]
    if len(strs) == 1:
        return s
    for i, c in enumerate(s):
        for j in range(1, len(strs)):
            t = strs[j]
            if i >= len(t) or c != t[i]:
                return s[:i]
    return s


class TestSolution(unittest.TestCase):
    def test_example(self):
        strs = ["flower", "flow", "flight"]
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "fl")

    def test_example_2(self):
        strs = ["dog", "racecar", "car"]
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "")

    def test_empty(self):
        strs = []
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "")
        strs = ["one"]
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "one")

    def test_long(self):
        strs = ["one1", "one2", "one3", "one4", "one5"]
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "one")

    def test_same_lengths(self):
        strs = ["a", "a"]
        ans = longest_common_prefix(strs)
        self.assertEqual(ans, "a")


if __name__ == "__main__":
    unittest.main()
