#! /usr/bin/env python
"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

    If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
    For example, the word 'apple' becomes 'applema'.

    If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
    For example, the word "goat" becomes "oatgma".

    Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
    For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin.



Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

Notes:
    S contains only uppercase, lowercase and spaces. Exactly one space between each word.
    1 <= S.length <= 150.
"""
import unittest


def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    l_words = []
    for i, word in enumerate(S.split()):
        if not is_vowel(word[0]):
            word = word[1:] + word[0]
        aa = "a" * (i + 1)
        l_words.append(word + "ma" + aa)
    return " ".join(l_words)


def is_vowel(c):
    return c.lower() in ["a", "e", "i", "o", "u"]


class TestSolution(unittest.TestCase):
    def test_example(self):
        s = "I speak Goat Latin"
        ans = toGoatLatin(s)
        self.assertEqual(ans, "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")

    def test_example_2(self):
        s = "The quick brown fox jumped over the lazy dog"
        ans = toGoatLatin(s)
        self.assertEqual(
            ans,
            "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa",
        )


if __name__ == "__main__":
    unittest.main()
