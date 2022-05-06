"""
49. Group Anagrams (Medium)

Given an array of strings strs, group the anagrams together. You can return the
answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

Constraints:

  1 <= strs.length <= 104
  0 <= strs[i].length <= 100
  strs[i] consists of lowercase English letters.
"""
from typing import List
import unittest


class Solution:

    """
    Patterns: Arrays, Hashing, Strings
    Time: O(n^2) where n is the number of strings.
    Space: O(n+n) where n is the number of strings.

    Iterate over each string and create an array of lowercase letter (a-z)
    counts. Convert this array into a key that represents the letters and
    counts. Anagrams will produce the same key as they have the same letters
    and counts. Use this key to group to the strings into groups.
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1
            key = tuple(counts)
            groups[key] = groups.get(key, [])
            groups[key].append(s)
        return list(groups.values())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        ans = self.solution.groupAnagrams(strs)
        assert ans == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    def test_example_2(self):
        strs = [""]
        ans = self.solution.groupAnagrams(strs)
        assert ans == [[""]]

    def test_example_3(self):
        strs = ["a"]
        ans = self.solution.groupAnagrams(strs)
        assert ans == [["a"]]
