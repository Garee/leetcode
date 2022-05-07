/**
 * 11. Container With Most Water (Medium)
 *
 * You are given an integer array height of length n. There are n vertical lines
 * drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 *
 * Find two lines that together with the x-axis form a container, such that the
 * container contains the most water.
 *
 * Return the maximum amount of water a container can store.
 *
 * Notice that you may not slant the container.
 *
 * Constraints
 *
 *   n == height.length
 *   2 <= n <= 105
 *   0 <= height[i] <= 104
 */

/**
 * Patterns: Arrays, Pointers
 * Time: O(n) where n is len(height)
 * Space: O(1)
 *
 * Create left/right pointers at each end of the array and move
 * then towards each other. At each step, take the min of the two heights
 * and multiply it by the distance between the pointers to calculate the area.
 * Track the max area found and return it as the result.
 *
 * @param {number[]} height the array of heights.
 * @return {number} the maximum amount of water.
 */
var maxArea = function (height) {
    let area = 0;

    let l = 0;
    let r = height.length - 1;
    while (l < r) {
        const h = Math.min(height[l], height[r]);
        const w = r - l;
        area = Math.max(area, h * w);
        if (height[l] < height[r]) {
            l++;
        } else {
            r--;
        }
    }

    return area;
};

test("example 1", () => {
    const height = [1, 8, 6, 2, 5, 4, 8, 3, 7];
    const ans = maxArea(height);
    expect(ans).toEqual(49);
});

test("example 2", () => {
    const height = [1, 1];
    const ans = maxArea(height);
    expect(ans).toEqual(1);
});
