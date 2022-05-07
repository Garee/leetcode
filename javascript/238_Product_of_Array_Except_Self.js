/**
 * 238. Product of Array Except Self (Medium)
 *
 * Given an integer array nums, return an array answer such that answer[i] is
 * equal to the product of all the elements of nums except nums[i].
 *
 * The product of any prefix or suffix of nums is guaranteed to fit in a
 * 32-bit integer.
 *
 * You must write an algorithm that runs in O(n) time and without using the
 * division operation.
 *
 * Constraints:
 *
 *    2 <= nums.length <= 105
 *   -30 <= nums[i] <= 30
 *   The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 */

/**
 * Patterns: Arrays
 * Time: O(n) where n is len(nums)
 * Space: O(n) where n is len(nums)
 *
 * Create a resulting array of size len(nums) and initialise it
 * with 1s. Iterate left to right through nums and update the result
 * array for the current num. Track the product as we iterate and use it
 * to set the current num, remembering to set the answer before updating
 * the product to ignore the current index. Next, perform the same
 * right to left.
 *
 * @param {number[]} nums the numbers to take the products of.
 * @return {number[]} the products of the numbers.
 */
var productExceptSelf = function (nums) {
    const result = new Array(nums.length).fill(1);

    let l = 1;
    for (let i = 0; i < nums.length; i++) {
        result[i] = l;
        l *= nums[i];
    }

    let r = 1;
    for (let i = nums.length - 1; i > -1; i--) {
        result[i] *= r;
        r *= nums[i];
    }

    return result;
};

test("example 1", () => {
    const nums = [1, 2, 3, 4];
    const ans = productExceptSelf(nums);
    expect(ans).toEqual([24, 12, 8, 6]);
});

test("example 2", () => {
    const nums = [-1, 1, 0, -3, 3];
    const ans = productExceptSelf(nums);
    expect(ans).toEqual([-0, 0, 9, -0, 0]);
});
