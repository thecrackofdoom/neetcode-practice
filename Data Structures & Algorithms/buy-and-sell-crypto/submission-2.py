class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit = max(prices[i:len(prices)]) - min(prices[0:i]) if max(prices[i:len(prices)]) - min(prices[0:i]) > profit else profit
        return profit
        