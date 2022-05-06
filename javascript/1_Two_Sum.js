/**
 * 1. Two Sum (Easy)
 *
 * Given an array of integers nums and an integer target, return indices of the
 * two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution, and you may
 * not use the same element twice.
 *
 * You can return the answer in any order.
 *
 * Constraints:
 *
 *   2 <= nums.length <= 104
 *  -109 <= nums[i] <= 109
 *  -109 <= target <= 109
 */

/**
 * Patterns: Arrays, Hashing
 * Time: O(n) where n is len(nums)
 * Space: O(n) where n is len(nums)
 *
 * Iterate through each num in nums and track each in a num->idx hash map.
 * If the matching paired number is already in the hash map, return its index
 * and the current index.
 *
 * @param {number[]} nums
 * @param {number} target
 * @return  {number[]}
 */
var twoSum = function (nums, target) {
    const met = {};

    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        const need = target - n;
        if (need in met) {
            return [met[need], i];
        }
        met[n] = i;
    }

    return [];
};

test("example 1", () => {
    const nums = [2, 7, 11, 15];
    const target = 9;
    const ans = twoSum(nums, target);
    expect(ans).toEqual([0, 1]);
});

test("example 2", () => {
    const nums = [3, 2, 4];
    const target = 6;
    const ans = twoSum(nums, target);
    expect(ans).toEqual([1, 2]);
});

test("example 3", () => {
    const nums = [3, 3];
    const target = 6;
    const ans = twoSum(nums, target);
    expect(ans).toEqual([0, 1]);
});
