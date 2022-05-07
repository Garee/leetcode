/**
 * 15. 3Sum
 *
 * Given an integer array nums, return all the triplets [nums[i]
 * , nums[j], nums[k]] such that i != j, i != k, and j != k, and
 * nums[i] + nums[j] + nums[k] == 0.
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 * Constraints
 *
 *   0 <= nums.length <= 3000
 * . -105 <= nums[i] <= 105
 */

/**
 * Patterns: Arrays, Pointers, Sorting
 * Time: O(n^2) where n is len(nums)
 * Space: O(1) (depends upon sorting implementation; may be O(n))
 *
 * This solution combines the Two Sum and Two Sum II problems. First,
 * sort the numbers and iterate through each. Skip duplicate numbers to the
 * rightmost one, so that they are only tried once. Next, create left/right
 * pointers and move them towards each other as you sum the triplets to check
 * that they equal zero. If a triplet is found, record it and go to the next
 * non-dup number and try again until the array is exhausted.
 *
 * @param {number[]} nums the numbers to search for triplets.
 * @return {number[][]} the triplets that sum to zero.
 */
var threeSum = function (nums) {
    const triplets = [];

    nums = nums.sort();
    nums.forEach((n, i) => {
        if (i > 0 && n === nums[i - 1]) {
            return;
        }

        let l = i + 1;
        let r = nums.length - 1;
        while (l < r) {
            const sum = n + nums[l] + nums[r];
            if (sum === 0) {
                triplets.push([n, nums[l], nums[r]]);
                l++;
                while (nums[l] === nums[l - 1] && l < r) {
                    l++;
                }
            } else if (sum > 0) {
                r--;
            } else {
                l++;
            }
        }
    });

    return triplets;
};

test("example 1", () => {
    const nums = [-1, 0, 1, 2, -1, -4];
    const ans = threeSum(nums);
    expect(ans).toEqual([
        [-1, -1, 2],
        [-1, 0, 1],
    ]);
});

test("example 2", () => {
    const nums = [];
    const ans = threeSum(nums);
    expect(ans).toEqual([]);
});

test("example 3", () => {
    const nums = [0];
    const ans = threeSum(nums);
    expect(ans).toEqual([]);
});
