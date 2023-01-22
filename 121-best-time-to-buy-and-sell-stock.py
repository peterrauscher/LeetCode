class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > best_profit:
                best_profit = price - min_price
        return best_profit