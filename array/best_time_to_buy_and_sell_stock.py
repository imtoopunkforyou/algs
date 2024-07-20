"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different
day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""


def max_profit(prices: list[int]) -> int:
    tb = []
    best: int = 0

    for idx in range(0, len(prices) - 1):
        for idx_next in range(idx + 1, len(prices)):
            if prices[idx] < prices[idx_next]:
                tb.append((prices[idx], prices[idx_next]))

    if not tb:
        return best

    for pair in tb:
        current = pair[1] - pair[0]
        best = current if current > best else best

    return best


if __name__ == '__main__':
    assert 5 == max_profit([7, 1, 5, 3, 6, 4])
    assert 0 == max_profit([7, 6, 4, 3, 1])
    assert 1 == max_profit([1, 2])
