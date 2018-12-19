#! /usr/bin/env python
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

    Input: "()"
    Output: true

Example 2:

    Input: "()[]{}"
    Output: true

Example 3:

    Input: "(]"
    Output: false

Example 4:

    Input: "([)]"
    Output: false

Example 5:

    Input: "{[]}"
    Output: true
"""
import unittest


def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    pairs = {"(": ")", "{": "}", "[": "]"}
    match = []
    for c in s:
        if c in pairs.keys():
            match.append(pairs[c])
        elif not match or c != match.pop():
            return False
    return len(match) == 0


class TestSolution(unittest.TestCase):
    def test_example(self):
        s = "()"
        ans = is_valid(s)
        self.assertTrue(ans)

    def test_example_2(self):
        s = "()[]{}"
        ans = is_valid(s)
        self.assertTrue(ans)

    def test_example_3(self):
        s = "(]"
        ans = is_valid(s)
        self.assertFalse(ans)

    def test_example_4(self):
        s = "([)]"
        ans = is_valid(s)
        self.assertFalse(ans)

    def test_example_5(self):
        s = "{[]}"
        ans = is_valid(s)
        self.assertTrue(ans)

    def test_empty(self):
        s = ""
        ans = is_valid(s)
        self.assertTrue(ans)

    def test_one_char(self):
        self.assertFalse(is_valid("["))
        self.assertFalse(is_valid("]"))


if __name__ == "__main__":
    unittest.main()
