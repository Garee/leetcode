/**
 * 121. Best Time To Buy And Sell Stock (Easy)
 *
 * You are given an array prices where prices[i] is the price of a given stock
 * on the ith day.
 *
 * You want to maximize your profit by choosing a single day to buy one stock
 * and choosing a different day in the future to sell that stock.
 *
 * Return the maximum profit you can achieve from this transaction. If you
 * cannot achieve any profit, return 0.
 *
 * Constraints
 *
 *  1 <= prices.length <= 105
 *  0 <= prices[i] <= 104
 */

/**
 * Patterns: Sliding Window
 * Time: O(n) where n is len(prices)
 * Space: O(1)
 *
 * @param {number[]} prices the stock prices.
 * @return {number} the maximum profit.
 */
var maxProfit = function (prices) {
    let profit = 0;

    let l = 0;
    for (let r = 1; r < prices.length; r++) {
        if (prices[r] < prices[l]) {
            l = r;
        }

        profit = Math.max(profit, prices[r] - prices[l]);
    }

    return profit;
};

test("example 1", () => {
    const prices = [7, 1, 5, 3, 6, 4];
    const ans = maxProfit(prices);
    expect(ans).toEqual(5);
});

test("example 2", () => {
    const prices = [7, 6, 4, 3, 1];
    const ans = maxProfit(prices);
    expect(ans).toEqual(0);
});
