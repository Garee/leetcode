/**
 * 424. Longest Repeating Character Replacement (Medium)
 *
 * Given a string that consists of only uppercase English letters,
 * you can replace any letter in the string with another letter at most k times.
 * Find the length of a longest substring containing all repeating letters you
 * can get after performing the above operations.
 *
 * Note: Both the string's length and k will not exceed 104.
 *
 * Constraints
 *
 *   1 <= s.length <= 105
 *   s consists of only uppercase English letters.
 *   0 <= k <= s.length
 */

/**
 * Patterns: Strings, Hashing, Sliding Window
 * Time: O(n) where n is len(s)
 * Space: O(1)
 *
 * @param {string} s the string to check.
 * @param {number} k the max number of repeats.
 * @returns the length of the longest substring containing all repeating letters.
 */
var characterReplacement = function (s, k) {
    let length = 0;

    const counts = {};
    let maxCount = 0;

    let l = 0;
    for (let r = 0; r < s.length; r++) {
        const c = s[r];

        const count = c in counts ? counts[c] + 1 : 1;
        counts[c] = count;
        maxCount = Math.max(maxCount, count);

        if (r - l + 1 - maxCount > k) {
            counts[s[l++]]--;
        }

        length = Math.max(length, r - l + 1);
    }

    return length;
};

test("example 1", () => {
    const s = "ABAB";
    const k = 2;
    const ans = characterReplacement(s, k);
    expect(ans).toEqual(4);
});

test("example 2", () => {
    const s = "AABABBA";
    const k = 1;
    const ans = characterReplacement(s, k);
    expect(ans).toEqual(4);
});
