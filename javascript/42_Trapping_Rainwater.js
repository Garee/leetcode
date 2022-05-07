/**
 * 42. Trapping Rainwater
 *
 * Given n non-negative integers representing an elevation map where the
 * width of each bar is 1, compute how much water it can trap after raining.
 *
 * Constraints
 *
 *   n == height.length
 *   1 <= n <= 2 * 104
 *   0 <= height[i] <= 105
 */

/**
 * Patterns: Arrays, Pointers
 * Time: O(n) where n is len(height)
 * Space: O(1)
 *
 * @param {number[]} height The elevation heights.
 * @return {number} the amount of water trapped.
 */
var trap = function (height) {
  let water = 0;

  let l = 0;
  let r = height.length - 1;
  let lMax = height[l];
  let rMax = height[r];
  while (l < r) {
    if (lMax < rMax) {
      lMax = Math.max(lMax, height[++l]);
      water += lMax - height[l];
    } else {
      rMax = Math.max(rMax, height[--r]);
      water += rMax - height[r];
    }
  }

  return water;
};

test("example 1", () => {
  const height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
  const ans = trap(height);
  expect(ans).toEqual(6);
});

test("example 2", () => {
  const height = [4, 2, 0, 3, 2, 5];
  const ans = trap(height);
  expect(ans).toEqual(9);
});
