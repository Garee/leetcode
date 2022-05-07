/**
 * 167. Two Sum II (Medium)
 *
 * Given a 1-indexed array of integers numbers that is already sorted
 * in non-decreasing order, find two numbers such that they add up to
 * a specific target number. Let these two numbers be numbers[index1]
 * and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
 *
 * Return the indices of the two numbers, index1 and index2, added by
 * one as an integer array [index1, index2] of length 2.
 *
 * The tests are generated such that there is exactly one solution. You
 * may not use the same element twice.
 *
 * Your solution must use only constant extra space.
 *
 * Constraints
 *
 *   2 <= numbers.length <= 3 * 104
 *   -1000 <= numbers[i] <= 1000
 * . numbers is sorted in non-decreasing order.
 *   -1000 <= target <= 1000
 *   The tests are generated such that there is exactly one solution.
 */

/**
 * Patterns: Arrays, Pointers
 * Time: O(n) where n is len(numbers)
 * Space: O(1)
 *
 * Create a left and right pointer at the ends of the numbers
 * array. Move them towards each other depending on whether the
 * sum of them is greater than or less than the target. Stop if they
 * sum to the target, or they meet at the same index.
 *
 * @param {number[]} numbers the numbers to search.
 * @param {number} target the target to sum to.
 * @return {number[]} the indices of the two numbers that sum to the target.
 */
var twoSum = function (numbers, target) {
    let l = 0;
    let r = numbers.length - 1;
    while (l < r) {
        const n = numbers[l] + numbers[r];
        if (n === target) {
            return [l + 1, r + 1];
        } else if (n > target) {
            r--;
        } else {
            l++;
        }
    }

    return [];
};

test("example 1", () => {
    const numbers = [2, 7, 11, 15];
    const target = 9;
    const ans = twoSum(numbers, target);
    expect(ans).toEqual([1, 2]);
});

test("example 2", () => {
    const numbers = [2, 3, 4];
    const target = 6;
    const ans = twoSum(numbers, target);
    expect(ans).toEqual([1, 3]);
});

test("example 3", () => {
    const numbers = [-1, 0];
    const target = -1;
    const ans = twoSum(numbers, target);
    expect(ans).toEqual([1, 2]);
});
