/**
 * 125. Valid Palindrome (Easy)
 *
 * A phrase is a palindrome if, after converting all uppercase letters
 * into lowercase letters and removing all non-alphanumeric characters,
 * it reads the same forward and backward. Alphanumeric characters include
 * letters and numbers.
 *
 * Given a string s, return true if it is a palindrome, or false otherwise.
 *
 * Constraints:
 *
 *   1 <= s.length <= 2 * 105
 *   s consists only of printable ASCII characters.
 */

/**
 * Patterns: Pointers, Strings
 * Time: O(n) where n is len(s)
 * Space: O(1)
 *
 * Create two pointers: one to the far left and one to the far
 * right of the lowercase string. Move the pointers towards each
 * other as you verify the characters are the same. Ignore non
 * alphanumeric characters and stop when the pointers reach the same
 * index.
 *
 * @param {string} s the string to check.
 * @return {boolean} true if the string is a palindrome; false otherwise.
 */
var isPalindrome = function (s) {
    s = s.toLowerCase();

    let l = 0;
    let r = s.length - 1;
    while (l < r) {
        while (l < r && !s[l].match(/[a-z0-9]/g)) {
            l++;
        }
        while (r > l && !s[r].match(/[a-z0-9]/g)) {
            r--;
        }
        if (s[l++] !== s[r--]) {
            return false;
        }
    }

    return true;
};

test("example 1", () => {
    const s = "A man, a plan, a canal: Panama";
    const ans = isPalindrome(s);
    expect(ans).toBe(true);
});

test("example 2", () => {
    const s = "race a car";
    const ans = isPalindrome(s);
    expect(ans).toBe(false);
});

test("example 3", () => {
    const s = " ";
    const ans = isPalindrome(s);
    expect(ans).toBe(true);
});
