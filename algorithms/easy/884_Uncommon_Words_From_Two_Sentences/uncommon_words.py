#! /usr/bin/env python
"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]

Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]

Note:

    0 <= A.length <= 200
    0 <= B.length <= 200
    A and B both contain only spaces and lowercase letters.
"""
import unittest
from collections import defaultdict


def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    counts = defaultdict(int)
    for word in A.split():
        counts[word] += 1
    for word in B.split():
        counts[word] += 1
    return [w for w in counts if counts[w] == 1]


class TestSolution(unittest.TestCase):
    def test_example(self):
        A = "this apple is sweet"
        B = "this apple is sour"
        ans = uncommonFromSentences(A, B)
        self.assertEqual(ans, ["sweet", "sour"])

    def test_example_2(self):
        A = "apple apple"
        B = "banana"
        ans = uncommonFromSentences(A, B)
        self.assertEqual(ans, ["banana"])


if __name__ == "__main__":
    unittest.main()
