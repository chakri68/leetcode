from typing import List, Optional


# Leetcode Problem 714: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
def calculateMaxProfit(prices: List[int], fee: int):
    cash = 0.0
    hold = float('-inf')

    for price in prices:
        prevCash = cash
        cash = max(cash, hold + price - fee)
        hold = max(hold, prevCash - price)

    return cash
