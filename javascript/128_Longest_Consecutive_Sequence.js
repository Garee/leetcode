/**
 * 128. Longest Consecutive Sequence (Medium)
 *
 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
 *
 * You must write an algorithm that runs in O(n) time.
 *
 * Constraints:
 *
 *   0 <= nums.length <= 105
 *   -109 <= nums[i] <= 109
 */

/**
 * Patterns: Arrays, Sets
 * Time: O(n) where n is len(nums)
 * Space: O(n) where n is len(nums)
 *
 * Create a unique set of the encountered nums. Iterate through
 * nums and detect if (num - 1) is not in the set, meaning this is
 * the start of a sequence. Increment the length while the sequence
 * exists in the set, and track the longest to return.
 *
 *
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
    let longest = 0;
    const s = new Set(nums);
    for (const n of nums) {
        if (!s.has(n - 1)) {
            let curr = 1;
            while (s.has(n + curr)) {
                curr++;
            }
            longest = Math.max(longest, curr);
        }
    }
    return longest;
};

test("example 1", () => {
    const nums = [100, 4, 200, 1, 3, 2];
    const ans = longestConsecutive(nums);
    expect(ans).toBe(4);
});

test("example 2", () => {
    const nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1];
    const ans = longestConsecutive(nums);
    expect(ans).toBe(9);
});
