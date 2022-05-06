/*
 * Given two strings s and t, return true if t is an anagram of s, and false
 * otherwise.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 * Constraints:
 *
 *   1 <= s.length, t.length <= 5 * 104
 *   s and t consist of lowercase English letters.
 */

/**
 * Pattern: Arrays, Hashing, Strings
 * Time: O(n + m) where n is len(s) and m is len(m)
 * Space: O(n + m) where n is len(s) and m is len(m)
 *
 * Return false if the two strings are different lengths as an
 * anagram must be the same length. Next, count the number of
 * occurences of each character in both strings. Finally, compare
 * these counts to make sure they are equal. Return false if they
 * are not equal, otherwise true.
 *
 * @param {string} s the first string.
 * @param {string} t the second string.
 * @return {boolean} true if s is an anagram of t.
 */
var isAnagram = function (s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const sCounts = {};
    const tCounts = {};
    for (let i = 0; i < s.length; i++) {
        sCounts[s[i]] = s[i] in sCounts ? sCounts[s[i]] + 1 : 0;
        tCounts[t[i]] = t[i] in tCounts ? tCounts[t[i]] + 1 : 0;
    }

    for (const [c, n] of Object.entries(sCounts)) {
        if (n !== tCounts[c]) {
            return false;
        }
    }

    return true;
};

test("example 1", () => {
    const s = "anagram";
    const t = "nagaram";
    const ans = isAnagram(s, t);
    expect(ans).toEqual(true);
});

test("example 2", () => {
    const s = "rat";
    const t = "car";
    const ans = isAnagram(s, t);
    expect(ans).toEqual(false);
});
