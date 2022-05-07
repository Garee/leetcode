/**
 * 3. Longest Substring Without Repeating Characters (Medium)
 *
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 *
 * Constraints
 *
 *   0 <= s.length <= 5 * 104
 *   s consists of English letters, digits, symbols and spaces.
 */

/**
 * Patterns: Sliding Window, Sets
 * Time: O(n) where n is len(s)
 * Space: O(n) where n is len(s)
 *
 * @param {string} s the string to check.
 * @return {number} the maximum substring length.
 */
var lengthOfLongestSubstring = function (s) {
    let length = 0;

    let chars = new Set();
    for (let l = 0, r = 0; r < s.length; r++) {
        while (chars.has(s[r])) {
            chars.delete(s[l++]);
        }
        chars.add(s[r]);
        length = Math.max(length, r - l + 1);
    }

    return length;
};

test("example 1", () => {
    //const s = "abcabcbb";
    const s = "dvdf";
    const ans = lengthOfLongestSubstring(s);
    expect(ans).toEqual(3);
});

test("example 2", () => {
    const s = "bbbbb";
    const ans = lengthOfLongestSubstring(s);
    expect(ans).toEqual(1);
});

test("example 3", () => {
    const s = "pwwkew";
    const ans = lengthOfLongestSubstring(s);
    expect(ans).toEqual(3);
});
