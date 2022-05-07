/**
 * 22. Generate Parenthesis (Medium)
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 * Constraints
 *
 *   1 <= n <= 8
 */

/**
 * Patterns: Stack
 * Time: O(n)
 * Space: O(n)
 *
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    const parens = [];

    function backtrack(opened = 0, closed = 0, stack = []) {
        console.log(opened, closed, stack);
        if (opened === closed && opened === n) {
            parens.push(stack.join(""));
            return;
        }

        if (opened < n) {
            stack.push("(");
            backtrack(opened + 1, closed, stack);
            stack.pop();
        }

        if (closed < opened) {
            stack.push(")");
            backtrack(opened, closed + 1, stack);
            stack.pop();
        }
    }

    backtrack();
    return parens;
};

test("example 1", () => {
    const n = 3;
    const ans = generateParenthesis(n);
    expect(ans).toEqual(["((()))", "(()())", "(())()", "()(())", "()()()"]);
});

test("example 2", () => {
    const n = 1;
    const ans = generateParenthesis(n);
    expect(ans).toEqual(["()"]);
});
