"""
Given two strings s and t, return true if t is an anagram of s, and false
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly
once.

Constraints:

  1 <= s.length, t.length <= 5 * 104
  s and t consist of lowercase English letters.
"""
import unittest
from collections import defaultdict


class Solution:

    """
    Pattern: Arrays, Hashing, Strings
    Time: O(n + m) where n is len(s) and m is len(m)
    Space: O(n + m) where n is len(s) and m is len(m)

    Return false if the two strings are different lengths as an
    anagram must be the same length. Next, count the number of
    occurences of each character in both strings. Finally, compare
    these counts to make sure they are equal. Return false if they
    are not equal, otherwise true.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counts = defaultdict(int)
        for c in s:
            s_counts[c] += 1
        t_counts = defaultdict(int)
        for c in t:
            t_counts[c] += 1
        for c, n in s_counts.items():
            if n != t_counts[c]:
                return False
        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "anagram"
        t = "nagaram"
        ans = self.solution.isAnagram(s, t)
        assert ans

    def test_example_2(self):
        s = "rat"
        t = "car"
        ans = self.solution.isAnagram(s, t)
        assert not ans
