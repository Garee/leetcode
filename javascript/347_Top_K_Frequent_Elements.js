/**
 * 347. Top K Frequent Elements (Medium)
 *
 * Given an integer array nums and an integer k, return the k most
 * frequent elements. You may return the answer in any order.
 *
 * Constraints:
 *
 *   1 <= nums.length <= 105
 *   k is in the range [1, the number of unique elements in the array].
 *   It is guaranteed that the answer is unique.
 */

/**
 * Patterns: Arrays, Hashing
 * Time: O(n) where n is len(nums)
 * Space: O(n) where n is len(nums)
 *
 * Iterate through each num and count the frequency of occurences
 * in a hash map. Get an array of unique nums and sort it by
 * frequency in ascending order. Take the first k elements from
 * this array as the result.
 *
 * @param {number[]} nums the numbers to get the most freq from.
 * @param {number} k the number of numbers to get.
 * @return {number[]} the top k most frequent numbers.
 */
var topKFrequent = function (nums, k) {
    const counts = new Map();
    for (const n of nums) {
        const count = counts.has(n) ? counts.get(n) : 0;
        counts.set(n, count + 1);
    }

    const uniqNums = [...counts.keys()];
    const sorted = uniqNums.sort((a, b) => {
        return counts.get(b) - counts.get(a);
    });

    return sorted.slice(0, k);
};

test("example 1", () => {
    const nums = [1, 1, 1, 2, 2, 3];
    const k = 2;
    const ans = topKFrequent(nums, k);
    expect(ans).toEqual([1, 2]);
});

test("example 2", () => {
    const nums = [1];
    const k = 1;
    const ans = topKFrequent(nums, k);
    expect(ans).toEqual([1]);
});

test("example 3", () => {
    const nums = [3, 0, 1, 0];
    const k = 1;
    const ans = topKFrequent(nums, k);
    expect(ans).toEqual([0]);
});
