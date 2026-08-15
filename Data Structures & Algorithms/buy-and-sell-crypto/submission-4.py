class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                max_p += prices[i] - prices[i - 1]
        return max_p