#! /usr/bin/env python
"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""
import unittest


def isAlienSorted(words: "List[str]", order: "str") -> "bool":
    orders = {c: i for i, c in enumerate(order)}
    for i in range(1, len(words)):
        prev, word = words[i - 1], words[i]
        for j in range(min(len(prev), len(word))):
            if prev[j] != word[j]:
                if orders[prev[j]] > orders[word[j]]:
                    return False
                break
            else:
                if len(prev) > len(word):
                    return False
    return True


class TestSolution(unittest.TestCase):
    def test_example(self):
        words = ["hello", "leetcode"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        ans = isAlienSorted(words, order)
        self.assertTrue(ans)

    def test_example_2(self):
        words = ["apple", "app"]
        order = "hlabcdefgijkmnopqrstuvwxyz"
        ans = isAlienSorted(words, order)
        self.assertFalse(ans)


if __name__ == "__main__":
    unittest.main()
