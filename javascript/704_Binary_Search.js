/**
 * 704. Binary Search (Easy)
 *
 * Given an array of integers nums which is sorted in ascending order,
 * and an integer target, write a function to search target in nums.
 * If target exists, then return its index. Otherwise, return -1.
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 * Constraints
 *
 *   1 <= nums.length <= 104
 *   -104 < nums[i], target < 104
 *   All the integers in nums are unique.
 *   nums is sorted in ascending order.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
    let l = 0;
    let r = nums.length - 1;
    while (l <= r) {
        const m = l + Math.floor((r - l) / 2);
        if (nums[m] === target) {
            return m;
        } else if (nums[m] < target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }

    return -1;
};

test("example 1", () => {
    const nums = [-1, 0, 3, 5, 9, 12];
    const target = 9;
    const ans = search(nums, target);
    expect(ans).toEqual(4);
});

test("example 2", () => {
    const nums = [-1, 0, 3, 5, 9, 12];
    const target = 2;
    const ans = search(nums, target);
    expect(ans).toEqual(-1);
});

test("example 2", () => {
    const nums = [5];
    const target = 5;
    const ans = search(nums, target);
    expect(ans).toEqual(0);
});
