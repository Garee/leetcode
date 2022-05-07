/*
 * 217. Contains Duplicate (Easy)
 *
 * Given an integer array nums, return true if any value appears at least twice
 * in the array, and return false if every element is distinct.
 *
 * Constraints:
 *
 *   1 <= nums.length <= 105
 *   -109 <= nums[i] <= 109
 */

/**
 * Patterns: Arrays, Sets
 * Time: O(n) where n is len(nums)
 * Space: O(n) where n is len(nums)
 *
 * Iterate through nums and track which nums have already been
 * met in a set. At each number, if it is already in the set it
 * is a duplicate, therefore return true.
 *
 * @param {number[]} nums the numbers to check.
 * @return {boolean} true if there is a duplicate number; otherwise false.
 */
var containsDuplicate = function (nums) {
    const s = new Set();

    for (const n of nums) {
        if (s.has(n)) {
            return true;
        }

        s.add(n);
    }

    return false;
};

test("example 1", () => {
    const nums = [1, 2, 3, 1];
    const ans = containsDuplicate(nums);
    expect(ans).toBe(true);
});

test("example 2", () => {
    const nums = [1, 2, 3, 4];
    const ans = containsDuplicate(nums);
    expect(ans).toBe(false);
});
