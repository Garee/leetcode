/**
 * 150. Evaluate Reverse Polish Notation (Medium)
 *
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 *
 * Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
 *
 * Note that division between two integers should truncate toward zero.
 *
 * It is guaranteed that the given RPN expression is always valid.
 * That means the expression would always evaluate to a result, and there will
 * not be any division by zero operation.
 *
 * Constraints
 *
 *   1 <= tokens.length <= 104
 *   tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
 */

/**
 * Patterns: Stack
 * Time: O(n) where n is len(tokens)
 * Space: O(n) where n is len(tokens)
 *
 * @param {string[]} tokens the tokens to evalute
 * @return {number} the result of the evaluation
 */
var evalRPN = function (tokens) {
    const stack = [];

    for (const token of tokens) {
        let a, b;
        switch (token) {
            case "+":
                stack.push(stack.pop() + stack.pop());
                break;
            case "-":
                a = stack.pop();
                b = stack.pop();
                stack.push(b - a);
                break;
            case "*":
                stack.push(stack.pop() * stack.pop());
                break;
            case "/":
                a = stack.pop();
                b = stack.pop();
                stack.push(parseInt(b / a));
                break;
            default:
                stack.push(parseInt(token));
        }
        console.log(token, stack);
    }
    return stack[0];
};

test("example 1", () => {
    const tokens = ["2", "1", "+", "3", "*"];
    const ans = evalRPN(tokens);
    expect(ans).toEqual(9);
});

test("example 2", () => {
    const tokens = ["4", "13", "5", "/", "+"];
    const ans = evalRPN(tokens);
    expect(ans).toEqual(6);
});

test("example 3", () => {
    const tokens = [
        "10",
        "6",
        "9",
        "3",
        "+",
        "-11",
        "*",
        "/",
        "*",
        "17",
        "+",
        "5",
        "+",
    ];
    const ans = evalRPN(tokens);
    expect(ans).toEqual(22);
});
