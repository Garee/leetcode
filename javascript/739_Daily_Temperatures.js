/**
 * 739. Daily Temperatures (Medium)
 *
 * Given an array of integers temperatures represents the daily temperatures,
 * return an array answer such that answer[i] is the number of days you have
 * to wait after the ith day to get a warmer temperature. If there is no future
 * day for which this is possible, keep answer[i] == 0 instead.
 *
 * Constraints
 *
 *   1 <= temperatures.length <= 105
 *   30 <= temperatures[i] <= 100
 */

/**
 * Patterns: Stack
 * Time: O(n) where n is len(temperatures)
 * Space: O(n) where n is len(temperatures)
 *
 * @param {number[]} temperatures the array of temperatures.
 * @return {number[]} the number of days between increases.
 */
var dailyTemperatures = function (temperatures) {
    const days = new Array(temperatures.length).fill(0);
    const stack = [];
    temperatures.forEach((t, i) => {
        while (stack.length && t > stack[stack.length - 1].temp) {
            const { idx } = stack.pop();
            days[idx] = i - idx;
        }
        stack.push({ temp: t, idx: i });
    });

    return days;
};

test("example 1", () => {
    const temperatures = [73, 74, 75, 71, 69, 72, 76, 73];
    const ans = dailyTemperatures(temperatures);
    expect(ans).toEqual([1, 1, 4, 2, 1, 1, 0, 0]);
});

test("example 2", () => {
    const temperatures = [30, 40, 50, 60];
    const ans = dailyTemperatures(temperatures);
    expect(ans).toEqual([1, 1, 1, 0]);
});

test("example 3", () => {
    const temperatures = [30, 60, 90];
    const ans = dailyTemperatures(temperatures);
    expect(ans).toEqual([1, 1, 0]);
});
