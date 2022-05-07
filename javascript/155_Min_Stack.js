/**
 * 155. Min Stack (Easy)
 *
 * Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
 *
 * Implement the MinStack class:
 * MinStack() initializes the stack object.
 * void push(int val) pushes the element val onto the stack.
 * void pop() removes the element on the top of the stack.
 * int top() gets the top element of the stack.
 * int getMin() retrieves the minimum element in the stack.
 *
 * Constraints
 *
 *   -231 <= val <= 231 - 1
 *   Methods pop, top and getMin operations will always be called on non-empty stacks.
 *   At most 3 * 104 calls will be made to push, pop, top, and getMin
 */

var MinStack = function () {
    this.min = [];
    this.stack = [];
};

/**
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function (val) {
    this.stack.push(val);
    const minVal = Math.min(val, this.getMin() ?? val);
    this.min.push(minVal);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function () {
    this.stack.pop();
    this.min.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function () {
    return this.stack[this.stack.length - 1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function () {
    return this.min[this.min.length - 1];
};

test("example 1", () => {
    const ms = new MinStack();
    ms.push(-2);
    ms.push(0);
    ms.push(-3);
    expect(ms.getMin()).toEqual(-3);
    ms.pop();
    expect(ms.top()).toEqual(0);
    expect(ms.getMin()).toEqual(-2);
});
