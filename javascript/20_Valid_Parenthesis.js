/**
 * 20. Valid Parenthesis (Easy)
 *
 * Given a string s containing just the characters
 * '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * An input string is valid if:
 *
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 *
 * Constraints
 *
 *   1 <= s.length <= 104
 *   s consists of parentheses only '()[]{}'
 */

/**
 * Patterns: Stack
 * Time: O(n) where n is len(s)
 * Space: O(n) where n is len(s)
 *
 * @param {string} s the string of parens.
 * @return {boolean} true if parens are all matched; false otherwise.
 */
var isValid = function (s) {
    const parens = {
        "(": ")",
        "{": "}",
        "[": "]",
    };

    const stack = [];
    for (const c of s) {
        if (c in parens) {
            stack.push(c);
        } else if (!stack.length || parens[stack.pop()] !== c) {
            return false;
        }
    }

    return stack.length === 0;
};

test("example 1", () => {
    const s = "()";
    const ans = isValid(s);
    expect(ans).toBe(true);
});

test("example 2", () => {
    const s = "()[]{}";
    const ans = isValid(s);
    expect(ans).toBe(true);
});

test("example 3", () => {
    const s = "(]";
    const ans = isValid(s);
    expect(ans).toBe(false);
});
