class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        runningMax = 0
        previousLow = prices[0]
        for price in prices[1:]:
            if price < previousLow:
                previousLow = price
            runningMax = max(runningMax, price - previousLow)
        return runningMax